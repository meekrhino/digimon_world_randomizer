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


def findSequenceInFile( filename, seq ):
    """
    Find the first occurence of the binary sequence in the file.
    """

    print( 'Finding seq: ' + str( seq ) )

    with open( filename, 'r+b' ) as file:
        mm = mmap.mmap( file.fileno(), 0 )
        found = []
        res = data.scriptOffsetInBinary
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

    print args

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