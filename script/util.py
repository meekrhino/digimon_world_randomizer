# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

"""
Utilities for writing specific positions in memory.
"""

import digimon.data as data
import struct
import mmap
#import pyperclip

setDialogOwner = 0x1B
setTrigger     = 0x1C
giveItem       = 0x28
spawnItem      = 0x74
learnMove      = 0x2D
spawnChest     = 0x75


def findAll( script, bin, inst, valueList=None ):
    """
    Find all uses of the given instruction.
    """

    with open( script, 'r' ) as file:
        out = []
        buf = '\n'
        while( buf != '' ):
            buf = file.readline()
            lineSplit = buf.split( ' ' )
            if( len( lineSplit ) > 1 ):
                if( lineSplit[1] == inst ):
                    args = []
                    for i in range( 2, len( lineSplit ) ):
                        args.append( int( lineSplit[i] ) )
                    if( valueList != None and ( args[0] not in valueList ) ):
                        continue
                    out.append( compile( inst, *args ) )

    ofst = []
    for seq in out:
        ofst.append( findSequenceInFile( bin, seq )  )

    if( len( out ) != len( ofst ) ):
        print( 'Error: unable to find some of the ' + inst + ' in the file: ' + str( len( ofst ) ) + '/' + str( len( out ) ) )

    strFormat = '(\n'

    for ofsts in ofst:
        strFormat += "(" + "".join("{:08X}, ".format(o) for o in ofsts) + "),\n"

    strFormat += ')'

    print( strFormat )
    #pyperclip.copy( strFormat )

    return ofst


def findAllDuplicatesForRecruitOffsets( filename ):
    """
    Find all offsets for duplicate recruitment data.
    """

    for ( triggers, val, id ) in data.recruitOffsets:
        #print( 'investigating triggers for digimon: ' + str( id ) )
        list = []
        for ofst in triggers:
            found = findAllDuplicatesOfDataAtOffset( filename, ofst, 20 )
            list += found
            #print( 'found ' + str( len( found ) ) + ' copies' )

        print( str( len( list ) ) + ': ( ' + ",".join("0x{:08X} ".format( o ) for o in list ) + ')' )


def findAllDuplicatesOfDataAtOffset( filename, ofst, sz ):
    """
    Find all occurences of the data that occurs at a given offset
    in the given file.  Match sz bytes.
    """

    with open( filename, 'r+b' ) as file:
        file.seek( ofst, 0 )
        seq = file.read( sz )

    found = findSequenceInFile( filename, seq )

    return found


def findSequenceInFile( filename, seq, ofst=None ):
    """
    Find the first occurence of the binary sequence in the file.
    """

    #print( 'Finding seq: ' + str( seq ) )

    with open( filename, 'r+b' ) as file:
        mm = mmap.mmap( file.fileno(), 0 )
        found = []
        if( ofst == None ):
            res = data.scriptOffsetInBinary
        else:
            res = ofst
        while( res != -1 and res < mm.size() ):
            res =  mm.find( seq, res + len( seq ) )
            if( res != -1 ):
                found.append( res )

    return found


def compile( inst, *args ):
    """
    Convert specified script instruction and args
    into hex instruction.

    Keyword arguments:
    inst -- Script instruction code.
    args -- Variable length argument list for instruction.
    """

    if( inst == 'spawnChest' ):
        packed = struct.pack(
                            '<BBhhhhh',
                            spawnChest,
                            args[0],
                            args[1],
                            args[2],
                            args[3],
                            args[4],
                            args[5]
                            )
    elif( inst == 'giveItem' ):
        packed = struct.pack(
                            '<BBBB',
                            giveItem,
                            0x00,
                            args[0],
                            args[1]
                            )
    elif( inst == 'spawnItem' ):
        packed = struct.pack(
                            '<BBhh',
                            spawnItem,
                            args[0],
                            args[1],
                            args[2]
                            )
    elif( inst == 'learnMove' ):
        packed = struct.pack(
                            '<BB',
                            learnMove,
                            args[0]
                            )
    elif( inst == 'move' ):
        packed = struct.pack(
                            '<BB',
                            learnMove,
                            args[0]
                            )
    elif( inst == 'setDialogOwner' ):
        packed = struct.pack(
                            '<BB',
                            setDialogOwner,
                            args[0]
                            )
    elif( inst == 'setTrigger' ):
        packed = struct.pack(
                            '<BxH',
                            setTrigger,
                            args[0]
                            )



    out =  "".join("{:02x}".format(ord(c)) for c in packed)
    print('Copied:'  + '\'' + out  + '\'' + ' to the cipboard')
    #pyperclip.copy(out)

    return ( packed )