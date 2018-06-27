# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Handler that stores all data associated with
a single digimon.
"""

import digimon.data as data
import script.util as scrutil
from future.utils import iteritems, itervalues


def typeIDToName( id ):
    """
    Convert type ID to name.

    Keyword argument:
    id -- Type ID to convert.
    """

    if( id in data.types ):
        return data.types[ id ]
    return "UNDEFINED"


def levelIDToName( id ):
    """
    Convert level ID to name.

    Keyword argument:
    id -- Level ID to convert.
    """

    if( id in data.levels ):
        return data.levels[ id ]
    return "UNDEFINED"


def specIDToName( id ):
    """
    Convert specialty ID to name.

    Keyword argument:
    id -- Specialty ID to convert.
    """

    if( id in data.specs ):
        return data.specs[ id ]
    return "-"


def itemIDToName( id ):
    """
    Convert item ID to name.

    Keyword argument:
    id -- Item ID to convert.
    """

    if( id in data.items ):
        return data.items[ id ]
    return "-"


def techIDToName( id ):
    """
    Convert tech ID to name.

    Keyword argument:
    id -- Tech ID to convert.
    """

    if( id in data.techs ):
        return data.techs[ id ]
    return "None"


class Digimon:
    """
    Digimon data object.  Stores all data about a given
    digimon.  (currently does not include raise data or
    evolution data)
    """

    def __init__( self, id, data ):
        """
        Separate out composite data into individual
        components.

        Keyword arguments:
        data -- List of values (unpacked from data string).
        """

        self.id        = id
        self.name      = data[ 0 ]
        self.models    = data[ 1 ]
        self.radius    = data[ 2 ]
        self.height    = data[ 3 ]
        self.type      = data[ 4 ]
        self.level     = data[ 5 ]

        self.spec = []
        for i in range( 3 ):
            self.spec.append( data[ 6 + i ] )

        self.item      = data[ 9 ]
        self.drop_rate = data[ 10 ]

        self.tech = []
        for i in range( 16 ):
            self.tech.append( data[ 11 + i ] )

    def __repr__( self ):
        """
        Produce a string representation of the object
        for convenient logging.
        """

        type  = typeIDToName( self.type )
        level = levelIDToName( self.level )
        item  = itemIDToName(  self.item )

        spec = []
        for i in range( 3 ):
            spec.append( specIDToName( self.spec[ i ] ) )

        repr = '{:>3d}{:>20s} {:>5d}{:>5d}{:>5d} {:>9s} {:>11s} {:>6s} {:>6s} {:>6s} {:>12s} {:>3d}%\n{:>23s} '.format(
                        self.id,
                        self.name.rstrip(' \t\r\n\0'),
                        self.models,
                        self.radius,
                        self.height,
                        type,
                        level,
                        spec[ 0 ], spec[ 1 ], spec[ 2 ],
                        item,
                        self.drop_rate,
                        "" )

        for i in range( 16 ):
            if( self.tech[ i ] != 'None' ):
                repr += techIDToName( self.tech[ i ] )
            if( i == 15 or techIDToName( self.tech[ i + 1 ] ) == 'None' ):
                break;
            repr +=  ', '

        return repr