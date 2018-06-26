# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Utilities for writing specific positions in memory.
"""

import digimon.data as data
import struct
import pyperclip

spawnChest = 0x75

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
        out =  "".join("{:02x}".format(c) for c in packed)
        print('Copied:'  + '\'' + out  + '\'' + ' to the cipboard')
        pyperclip.copy(out)
    return ( packed )