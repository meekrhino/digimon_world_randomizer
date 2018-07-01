# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Handler that stores all data associated with
a single digimon.
"""

import digimon.data as data, digimon.util as util
import script.util as scrutil
from future.utils import iteritems, itervalues


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

        #decode binary data as ascii and trim trailing nulls
        self.name      = data[ 0 ].decode( 'ascii' ).rstrip( '\0' )
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


    def __str__( self ):
        """
        Produce a string representation of the object
        for convenient logging.
        """

        type  = util.typeIDToName( self.type )
        level = util.levelIDToName( self.level )

        spec = []
        for i in range( 3 ):
            spec.append( util.specIDToName( self.spec[ i ] ) )

        out = '{:>3d}{:>20s} {:>5d}{:>5d}{:>5d} {:>9s} {:>11s} {:>6s} {:>6s} {:>6s} {:>3d} {:>3d}%\n{:>23s} '.format(
                        self.id,
                        self.name.rstrip(' \t\r\n\0'),
                        self.models,
                        self.radius,
                        self.height,
                        type,
                        level,
                        spec[ 0 ], spec[ 1 ], spec[ 2 ],
                        self.item,
                        self.drop_rate,
                        "" )

        for i in range( 16 ):
            if( self.tech[ i ] != 'None' ):
                out += util.techIDToName( self.tech[ i ] )
            if( i == 15 or util.techIDToName( self.tech[ i + 1 ] ) == 'None' ):
                break;
            out +=  ', '

        return out


    def unpackedFormat( self ):
        """
        Produce a tuple representation of all
        of the data in the object.
        """
        repr = []

        repr.append( self.name.encode( 'ascii' ) )  # 0
        repr.append( self.models )                  # 1
        repr.append( self.radius )                  # 2
        repr.append( self.height )                  # 3
        repr.append( self.type )                    # 4
        repr.append( self.level )                   # 5

        for spec in self.spec:
            repr.append( spec )                     # 6 7 8

        repr.append( self.item )                    # 9
        repr.append( self.drop_rate )               # 10

        for tech in self.tech:
            repr.append( tech )                     # 11+

        return tuple( repr )


class Item:
    """
    Item data object.  Stores all data about a given
    item.
    """

    #Grey Claws - Moon mirror, Giga Hand, Noble Mane, Metalbanana
    evoItems = list( range( 0x47, 0x73 ) ) + [ 0x7D, 0x7E, 0x7F ]
    consumableItems = list( range( 0x00, 0x21 ) ) + list( range( 0x26, 0x73 ) ) + [ 0x7A, 0x7B, 0x7D, 0x7E, 0x7F ]
                    
    def __init__( self, id, data ):
        """
        Separate out composite data into individual
        components.

        Keyword arguments:
        data -- List of values (unpacked from data string).
        """
        self.id       = id

        #decode binary data as ascii and trim trailing nulls
        self.name     = data[ 0 ].decode( 'ascii' ).rstrip( '\0' )
        self.price    = data[ 1 ]
        self.merit    = data[ 2 ]
        self.sort     = data[ 3 ]
        self.color    = data[ 4 ]
        self.dropable = data[ 5 ]

        self.isEvo = id in self.evoItems
        self.isConsumable = id in self.consumableItems


    def __str__( self ):
        """
        Produce a string representation of the object
        for convenient logging.
        """

        out = '{:>3d}{:>20s} {:>4d} {:>4d} {:>2d} {:>2d} {!r:>5}'.format(
                        self.id,
                        self.name,
                        self.price,
                        self.merit,
                        self.sort,
                        self.color,
                        self.dropable )

        return out


    def unpackedFormat( self ):
        """
        Produce a tuple representation of all
        of the data in the object.
        """
        repr = []

        repr.append( self.name.encode( 'ascii' ) )  # 0
        repr.append( self.price )                   # 1
        repr.append( self.merit )                   # 2
        repr.append( self.sort )                    # 3
        repr.append( self.color )                   # 4
        repr.append( self.dropable )                # 5

        return tuple( repr )


    def isAllowedInChest( self, allowEvos ):
        """
        Check if this items should be allowed in chests,
        allowing or disallowing evos as necessary.  Always
        ban quest items (undroppable).
        """
        if( allowEvos ):
            return self.dropable
        else:
            return ( self.dropable and not self.isEvo )
            
            
    def isAllowedTokomon( self, onlyConsumables ):
        """
        Check if this items should be allowed in chests,
        allowing or disallowing evos as necessary.  Always
        ban quest items and evos (game breaking).
        """
        if( onlyConsumables ):
            return ( self.isConsumable and not self.isEvo )
        else:
            return ( self.dropable and not self.isEvo )

