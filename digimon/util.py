# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Utilities for manipulating digimon data.
"""

import digimon.data as data
import sys

def writeDataToFile( file, ofst, str, verbose ):
    """
    Convert specified value to bytes and write to file.

    Keyword arguments:
    file -- File pointer opened in binary mode.
    ofst -- Offset to write.
    value -- Value to write.
    """
    file.seek( ofst, 0 )

    if( verbose ):
        print( 'Writing the following to file: ' + str )

    return file.write( str )


def techSlotAnimID( slot ):
    """
    Get the animation ID for the specified tech slot.

    Keyword arguments:
    slot -- Tech slot to convert (1 to 16)
    """

    if( slot < 1 or slot > 16 ):
        print( 'Error: Tried to use an invalid tech slot: ' + format( slot, '02x' ) )
        slot = 1

    #Move slots index from 1 and the move animations index from 0x2E
    #So slot 1 in animation 0x2E
    return 0x2E + (slot - 1)

def animIDTechSlot( anim ):
    """
    Get the tech slot for the specified animation ID.

    Keyword arguments:
    anim -- Animation ID to convert (2E to 3D)
    """

    #Move slots index from 1 and the move animations index from 0x2E
    #So slot 1 in animation 0x2E
    slot = anim - 0x2E + 1

    if( slot < 1 or slot > 16 ):
        print( 'Error: Tried to read an invalid animation ID as a tech slot: ' + format( slot, '02x' ) )
        slot = 1

    return slot

def starterTech( id ):
    """
    Get the starter tech ID for the specified starter digimon ID.

    Keyword arguments:
    id -- Digimon ID to get starter tech for
    """
    if( id not in data.starterTechs ):
        print( 'Error: Tried to get starter tech for invalid digimon: ' + format( id, '02x' ) )
        id = data.rookies[ 0 ]

    return data.starterTechs[ id ]

def starterTechSlot( id ):
    """
    Get the starter tech slot for the specified starter digimon ID.

    Keyword arguments:
    id -- Digimon ID to get starter tech slot for
    """
    if( id not in data.starterTechSlots ):
        print( 'Error: Tried to get starter tech slot for invalid digimon: ' + format( id, '02x' ) )
        id = data.rookies[ 0 ]

    return data.starterTechSlots[ id ]