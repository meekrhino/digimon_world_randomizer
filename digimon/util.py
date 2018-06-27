# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Utilities for manipulating digimon data.
"""

import digimon.data as data
from digimon.digimonclass import Digimon
import sys
import struct


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


def readDataWithExclusions( file, ofst, sz, excls, excl_sz ):
    """
    Read data from file, excluding selected sections.

    Keyword arguments:
    file -- File pointer.
    ofst -- Offset to start reading from.
    sz   -- Length of data block to read (includes
            exclusion sections).
    excls -- List of offset exclusion starting points.
    excl_sz -- Size of exclusions (all must be same size).
    """

    file.seek( ofst, 0 )
    out = ''

    bytes_read = 0
    for nextExcl in excls:
        pos = ofst + bytes_read
        bytes_to_read = nextExcl - pos
        out += file.read( bytes_to_read )
        file.seek( excl_sz, 1 )
        bytes_read += bytes_to_read + excl_sz

    out += file.read( sz - bytes_read )

    return out


def parseDataArray( buf, fmt, count ):
    """
    Parse data as an array of structs.

    Keyword arguments:
    buf -- String of data.
    fmt -- Struct format.
    count -- Length of array.
    """

    fmt_sz = struct.calcsize( fmt )

    data = []

    if not count * fmt_sz == len( buf ):
        print( 'Error: trying to parse data array with size '
             + 'not matching expected size.' )
        return []

    for i in range( count ):
        data.append( Digimon( i, struct.unpack_from( fmt, buf, i * fmt_sz ) ) )

    return data


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
    id -- Digimon ID to get starter tech for.
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

