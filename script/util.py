# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Utilities for writing specific positions in memory.
"""

import digimon.data as data
import struct
import mmap
import pyperclip

giveItem = 0x28
spawnChest = 0x75
spawnItem = 0x74


def findAll( script, bin, inst ):
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
                    out.append( compile( inst, *args ) )
                    
    ofst = []
    for seq in out:
        ofst.append( findSequenceInFile( bin, seq )  )
    
    if( len( out ) != len( ofst ) ):
        print( 'Error: unable to find some of the ' + inst + ' in the file: ' + str( len( ofst ) ) + '/' + str( len( out ) ) )
    
    strFormat = '(\n'
    
    for o in ofst:
        strFormat += format( o, '08X' ) + ',\n'
        
    strFormat += ')'
    
    print( strFormat )
    pyperclip.copy( strFormat )
    
    return ofst
    
    
    
def findSequenceInFile( filename, seq ):
    """
    Find the first occurence of the binary sequence in the file.
    """
    
    print( 'Finding seq: ' + str( seq ) )
    
    with open( filename, 'r+b' ) as file:
        mm = mmap.mmap( file.fileno(), 0 )
        res = mm.find( seq ) 
        return res
        

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
                            '<BBbbhbbhh', 
                            spawnChest,
                            args[0],
                            args[1],
                            args[2],
                            args[3],
                            args[4],
                            args[5],    
                            args[6],
                            args[7]
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
                            
       
    #out =  "".join("{:02x}".format(c) for c in packed)
    #print('Copied:'  + '\'' + out  + '\'' + ' to the cipboard')
    #pyperclip.copy(out)
    
    return ( packed )