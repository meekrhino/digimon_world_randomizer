# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

"""
Handler that stores all data to be written to the ROM.
Classes to represent data inside the ROM.
"""

import digimon.data as data, digimon.util as util
import script.util as scrutil
from log.logger import Logger

import random, struct, sys
from shutil import copyfile
from future.utils import iteritems, itervalues


class Digimon:
    """
    Digimon data object.  Stores all data about a given
    digimon.  (currently does not include raise data or
    evolution data)
    """

    #Everything up to MetalEtemon minus WereGarurumon (not implemented!)
    #Panjyamon, Gigadramon, and Metaletemon need evo req updates to be
    #added back in.
    playableDigimon = list( range( 0x01, 0x3E ) )# + [ 0x3F, 0x40, 0x41 ]


    def __init__( self, handler, id, data ):
        """
        Separate out composite data into individual
        components.

        Keyword arguments:
        data -- List of values (unpacked from data string).
        """

        self.handler   = handler
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

        self.fromEvo = []
        for i in range( 5 ):
            self.fromEvo.append( 0xFF )

        self.toEvo = []
        for i in range( 6 ):
            self.toEvo.append( 0xFF )


    def __str__( self ):
        """
        Produce a string representation of the object
        for convenient logging.
        """

        type  = self.handler.getTypeName( self.type )
        level = self.handler.getLevelName( self.level )
        item  = self.handler.getItemName( self.item )

        spec = []
        for i in range( 3 ):
            spec.append( self.handler.getSpecialtyName( self.spec[ i ] ) )

        out = '{:>3d}{:>20s} {:>5d}{:>5d}{:>5d} {:>9s} {:>11s} {:>6s} {:>6s} {:>6s} {:>12s} {:>3d}%\n{:>23s} '.format(
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
                out += self.handler.getTechName( self.tech[ i ] )
            if( i == 15 or self.handler.getTechName( self.tech[ i + 1 ] ) == 'None' ):
                break;
            out +=  ', '

        return out


    def setEvoData( self, data ):
        """
        Separate out composite data into individual
        components and attach to existing Digimon.

        Keyword arguments:
        data -- List of values (unpacked from data string).
        """


        for i in range( 5 ):
            self.fromEvo[ i ] = data[ i ]

        for i in range( 6 ):
            self.toEvo[ i ] = data[ 5 + i ]


    def evoData( self ):
        """
        Produce a string representation of the Digimon's evo
        data for convenient logging.
        """

        out = self.name + '\nNow evolves from '

        for i in range( 5 ):
            out += self.handler.getDigimonName( self.fromEvo[ i ] ) + ' '

        out += '\nNow evolves to '

        for i in range( 6 ):
            out += self.handler.getDigimonName( self.toEvo[ i ] ) + ' '

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


    def unpackedEvoFormat( self ):
        """
        Produce a tuple representation of the evo
        data for the object.
        """

        repr = []

        for e in self.fromEvo:
            repr.append( e )

        for e in self.toEvo:
            repr.append( e )

        return tuple( repr )


    def getEvoToCount( self ):
        """
        Get current number of digimon this digimon
        can evolve to.
        """

        sum = 0;
        for e in self.toEvo:
            if( e != 0xFF ):
                sum += 1

        return sum


    def getEvoFromCount( self ):
        """
        Get current number of digimon this digimon
        can evolve from.
        """

        sum = 0;
        for e in self.fromEvo:
            if( e != 0xFF ):
                sum += 1

        return sum


    def clearEvos( self ):
        """
        Clear all of this digimon's evos to/from.
        """

        for i in range( 5 ):
            self.fromEvo[ i ] = 0xFF

        for i in range( 6 ):
            self.toEvo[ i ] = 0xFF


    def updateEvosFrom( self ):
        """
        Update this digimon's list of digimon that
        can evolve into it.
        """

        evos = []
        for digi in self.handler.digimonData:
            if( self.id in digi.toEvo ):
                evos.append( digi.id )

        #This is the order in which evos are filled
        #i.e. if there are two evos, they are in
        #the 3rd slot and the 2nd slot (#2, #1)
        #Copy up to 5 evos in.  If less, fill with
        #0xFF, aka none.  Truncate extras.
        for i, j in enumerate( [ 2, 1, 3, 0, 4 ] ):
            if( i < len( evos ) ):
                self.fromEvo[ j ] = evos[ i ]
            else:
                self.fromEvo[ j ] = 0xFF


    def validEvosTo( self ):
        """
        Produce list of valid digimon IDs that this
        digimon could potentially evolve to.
        """

        #Find all digimon that are playable and one level above
        validEvos = self.handler.getPlayableDigimonByLevel( self.level + 1 )

        exclusionList = []
        i = 0
        while( i < len( validEvos ) ):
            if( validEvos[ i ].name in [ 'Kunemon', 'Devimon', 'Numemon', 'Sukamon', 'Nanimon', 'Vademon' ] ):
                del validEvos[ i ]
            else:
                i += 1

        return validEvos


    def addEvoTo( self, id ):
        """
        Add a new evolution target to this digimon.

        Keyword arguments:
        id -- ID of digimon to add as evolution.
        """

        #Search in the order that evos are filled
        for i in [ 2, 3, 1, 4, 0, 5 ]:
            #If this digimon already has this evo,
            #don't add it again.
            if( self.toEvo[ i ] == id ):
                break;

            #If we found an empty slot and the
            #digimon doesn't have this evo, add
            #if to the list.
            if( self.toEvo[ i ] == 0xFF ):
                self.toEvo[ i ] = id
                break


class Item:
    """
    Item data object.  Stores all data about a given
    item.
    """

    itemSort = {
            0x00 : 'HEAL',
            0x01 : 'STATUS',
            0x02 : 'FOOD',
            0x03 : 'BATTLE',
            0x04 : 'STATEVO',
            0x05 : 'PASSIVEQUEST'
            }

    consumableItems = list( range( 0x00, 0x21 ) ) + list( range( 0x26, 0x73 ) ) + [ 0x79, 0x7A, 0x7D, 0x7E, 0x7F ]

    def __init__( self, handler, id, data ):
        """
        Separate out composite data into individual
        components.

        Keyword arguments:
        data -- List of values (unpacked from data string).
        """

        self.handler  = handler
        self.id       = id

        #decode binary data as ascii and trim trailing nulls
        self.name     = data[ 0 ].decode( 'ascii' ).rstrip( '\0' )
        self.price    = data[ 1 ]
        self.merit    = data[ 2 ]
        self.sort     = data[ 3 ]
        self.color    = data[ 4 ]
        self.dropable = data[ 5 ]

        #Exclude the Stat items, which share a sort value with the Evo items
        self.isEvo = ( self.itemSort[ self.sort ] == 'STATEVO' and id >= 0x47 )
        self.isConsumable = id in self.consumableItems

        #'Food' sort value is not used for 'Rain Plant' and 'Steak'
        self.isFood = self.itemSort[ self.sort ] == 'FOOD' or id == 0x79 or id == 0x7A


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


class Tech:
    """
    Tech data object.  Stores all data about a given
    tech.  Currently only names (read ONLY)
    """

    finishers = list( range( 0x3A, 0x71 ) )

    def __init__( self, handler, id, data ):
        """
        Separate out composite data into individual
        components.

        Keyword arguments:
        data -- List of values (unpacked from data string).
        """

        self.handler  = handler
        self.id       = id

        self.name     = 'None'
        self.tier     = 0xFF

        self.power    = data[ 0 ]
        self.mp3      = data[ 1 ]
        self.itime    = data[ 2 ]
        self.range    = data[ 3 ]
        self.spec     = data[ 4 ]
        self.effect   = data[ 5 ]
        self.accuracy = data[ 6 ]
        self.effChance= data[ 7 ]
        self.aiDist   = data[ 8 ]

        self.isDamaging = self.power > 0
        self.isFinisher = self.id in self.finishers


    def __str__( self ):
        """
        Produce a string representation of the object
        for convenient logging.
        """

        out = '{:>3d} {:<20s} (Tier: {:<2d})\n   {:>3d} {:>3d} {:>2d} {:>5s} {:>6s} {:>7s} {:>3d} {:>3d}% {:>2d}'.format(
                        self.id,
                        self.name,
                        self.tier,
                        self.power,
                        self.mp3 * 3,
                        self.itime,
                        self.handler.getRangeName( self.range ),
                        self.handler.getSpecialtyName( self.spec ),
                        self.handler.getEffectName( self.effect ),
                        self.accuracy,
                        self.effChance,
                        self.aiDist )

        return out


    def unpackedFormat( self ):
        """
        Produce a tuple representation of all
        of the data in the object.
        """
        repr = []

        repr.append( self.power )
        repr.append( self.mp3 )
        repr.append( self.itime )
        repr.append( self.range )
        repr.append( self.spec )
        repr.append( self.effect )
        repr.append( self.accuracy )
        repr.append( self.effChance )
        repr.append( self.aiDist )

        return tuple( repr )


    def setName( self, name ):
        """
        Assign a name to the tech

        Keyword arguments:
        name -- Name to set.
        """

        self.name     = name


class DigimonWorldHandler:
    """
    Digimon World handler class.  Holds all data
    that can be modified and written out to the
    file.
    """

    #       Endianness                      Size (packed/not)
    # @     native                          native
    # =     native                          standard
    # <     little-endian                   standard
    # >     big-endian                      standard
    # !     network (= big-endian)          standard

    #       Type
    # x     pad byte
    # c     char
    # b     signed char
    # B     unsigned char
    # ?     _Bool
    # h     short
    # H     unsigned short
    # i     int
    # I     unsigned int
    # l     long
    # L     unsigned long
    # q     long long
    # Q     unsigned long long
    # f     float
    # d     double
    # s     char[]
    # p     char[]
    # P     void *

    def __init__( self, filename, logger, seed=None ):
        """
        Load ROM data into cache so that it can be read
        and manipulated.

        Keyword arguments:
        filename -- Name of file to read.
        seed -- Randomizer seed.
        """

        self.logger = logger

        self.randomseed = seed
        if( seed == None ):
            self.randomseed = random.randrange( sys.maxsize )
        random.seed( a=self.randomseed )

        self.inFilename = filename

        try:
            file = open( filename, 'r' + 'b' )
        except IOError:
            self.logger.fatalError( 'Error: input file could not be read (it probably doesn\'t exist)\nMake sure the filename and relative path in settings.ini \'Input\' are correct.' )

        with file:
            #------------------------------------------------------
            # Read in tech data
            #------------------------------------------------------

            #Read in full item data block
            data_read = util.readDataWithExclusions( file,
                                                     data.techDataBlockOffset,
                                                     data.techDataBlockSize,
                                                     data.techDataExclusionOffsets,
                                                     data.techDataExclusionSize )

            #Parse data block
            data_unpacked = util.unpackDataArray( data_read,
                                                  data.techDataFormat,
                                                  data.techDataBlockCount )

            #Store data in item objects
            self.techData = []
            for i, data_tuple in enumerate( data_unpacked ):
                self.techData.append( Tech( self, i, data_tuple ) )
                self.techData[ i ].setName( data.techs[ i ] )


            #------------------------------------------------------
            # Read in tech tier list
            #------------------------------------------------------

            #Read in tier list data block
            data_read = util.readDataWithExclusions( file,
                                                     data.techTierListBlockOffset,
                                                     data.techTierListBlockSize,
                                                     data.techTierListExclusionOffsets,
                                                     data.techTierListExclusionSize )

            #Parse data block
            data_unpacked = util.unpackDataArray( data_read,
                                                  data.techTierListFormat,
                                                  data.techTierListBlockCount )

            #Extract tiers for all techs
            for data_tuple in data_unpacked:
                for i, techID in enumerate( data_tuple ):
                    self.techData[ techID ].tier = i + 1

            for tech in self.techData:
                self.logger.log( str( tech ) )


            #------------------------------------------------------
            # Read in item data
            #------------------------------------------------------

            #Read in full item data block
            data_read = util.readDataWithExclusions( file,
                                                     data.itemDataBlockOffset,
                                                     data.itemDataBlockSize,
                                                     data.itemDataExclusionOffsets,
                                                     data.itemDataExclusionSize )

            #Parse data block
            data_unpacked = util.unpackDataArray( data_read,
                                                  data.itemDataFormat,
                                                  data.itemDataBlockCount )

            #Store data in item objects
            self.itemData = []
            for i, data_tuple in enumerate( data_unpacked ):
                self.itemData.append( Item( self, i, data_tuple ) )
                self.logger.log( str( self.itemData[ i ] ) )


            #------------------------------------------------------
            # Read in digimon data
            #------------------------------------------------------

            #Read in full digimon stats data block
            data_read = util.readDataWithExclusions( file,
                                                     data.digimonDataBlockOffset,
                                                     data.digimonDataBlockSize,
                                                     data.digimonDataExclusionOffsets,
                                                     data.digimonDataExclusionSize )

            #Parse data block
            data_unpacked = util.unpackDataArray( data_read,
                                                  data.digimonDataFormat,
                                                  data.digimonDataBlockCount )

            #Store data in digimon objects
            self.digimonData = []
            for i, data_tuple in enumerate( data_unpacked ):
                self.digimonData.append( Digimon( self, i, data_tuple ) )
                self.logger.log( str( self.digimonData[ i ] ) + '\n' )


            #------------------------------------------------------
            # Read in evo data
            #------------------------------------------------------

            #Read in evo to/from data block
            data_read = util.readDataWithExclusions( file,
                                                     data.evoToFromBlockOffset,
                                                     data.evoToFromBlockSize,
                                                     data.evoToFromExclusionOffsets,
                                                     data.evoToFromExclusionSize )

            #Parse data block
            data_unpacked = util.unpackDataArray( data_read,
                                                  data.evoToFromFormat,
                                                  data.evoToFromBlockCount )

            #Store data in digimon objects
            for i, data_tuple in enumerate( data_unpacked ):
                #Index from 1 because player (ID#0) does not have evo entries
                self.digimonData[ 1 + i ].setEvoData( data_tuple )
                self.logger.log( self.digimonData[ 1 + i ].evoData() + '\n' )


            #------------------------------------------------------
            # Read in starter data
            #------------------------------------------------------
            self.starterID = []
            self.starterTech = []
            self.starterTechSlot = []

            for i in [ 0, 1 ]:
                #Read in first starter digimon ID
                file.seek( data.starterSetDigimonOffset[ i ], 0 )
                self.starterID.append( struct.unpack( data.digimonIDFormat, file.read( 1 ) )[0] )
                self.logger.log( self.digimonData[ self.starterID[ i ] ].name )

                #Read in first starter learned tech ID
                file.seek( data.starterLearnTechOffset[ i ], 0 )
                self.starterTech.append( struct.unpack( data.techIDFormat, file.read( 1 ) )[0] )
                self.logger.log( '0x' + format( self.starterTech[ i ], '02x' ) + ' = tech ID' )

                #Read in first starter learned tech slot
                file.seek( data.starterEquipAnimOffset[ i ], 0 )
                self.starterTechSlot.append( util.animIDTechSlot( struct.unpack( data.animIDFormat, file.read( 1 ) )[0] ) )
                self.logger.log( '0x' + format( self.starterTechSlot[ i ], '02x' ) + ' = tech slot' )


            #------------------------------------------------------
            # Read in chest item data
            #------------------------------------------------------

            self.chestItems = {}

            for ofst in data.chestItemOffsets:
                file.seek( ofst, 0 )
                cmd, item = struct.unpack( data.chestItemFormat,
                                           file.read( struct.calcsize( data.chestItemFormat ) ) )
                if( cmd != scrutil.spawnChest ):
                    self.logger.logError( 'Error: Looking for chest item, found incorrect command: ' + str( cmd ) + ' @ ' + format( ofst, '08x' ) )
                else:
                    self.chestItems[ ofst ] = item

            for item in itervalues( self.chestItems ):
                self.logger.log( 'Chest contains: \'' + self.itemData[ item ].name + '\'' )

            #------------------------------------------------------
            # Read in map item spawn data
            #------------------------------------------------------

            self.mapItems = {}

            for ofst in data.mapItemOffsets:
                file.seek( ofst, 0 )
                cmd, item = struct.unpack( data.mapItemFormat,
                                           file.read( struct.calcsize( data.mapItemFormat ) ) )
                if( cmd != scrutil.spawnItem ):
                    self.logger.logError( 'Error: Looking for map item, found incorrect command: ' + str( cmd ) + ' @ ' + format( ofst, '08x' ) )
                else:
                    self.logger.log( ' \'' + self.itemData[ item ].name + '\' spawns on the map.' )
                    self.mapItems[ ofst ] = item


            #------------------------------------------------------
            # Read in Tokomon item data
            #------------------------------------------------------

            self.tokoItems = {}

            for ofst in data.tokoItemOffsets:
                file.seek( ofst, 0 )
                cmd, item, count = struct.unpack( data.tokoItemFormat,
                                                  file.read( struct.calcsize( data.tokoItemFormat ) ) )
                if( cmd != scrutil.giveItem ):
                    self.logger.logError( 'Error: Looking for Tokomon item, found incorrect command: ' + str( cmd ) + ' @ ' + format( ofst, '08x' ) )
                else:
                    self.tokoItems[ ofst ] = ( item, count )

            for ( item, count ) in itervalues( self.tokoItems ):
                self.logger.log( 'Tokomon gives: ' + str( count ) + 'x \'' + self.itemData[ item ].name + '\'' )


            #------------------------------------------------------
            # Read in tech gift data
            #------------------------------------------------------

            self.techGifts = {}

            for ofst in data.learnMoveOffsets:
                file.seek( ofst, 0 )
                cmd, tech = struct.unpack( data.learnMoveFormat,
                                           file.read( struct.calcsize( data.learnMoveFormat ) ) )
                if( cmd != scrutil.learnMove ):
                    self.logger.logError( 'Error: Looking for tech learning gift, found incorrect command: ' + str( cmd ) + ' @ ' + format( ofst, '08x' ) )
                else:
                    self.techGifts[ ofst ] = tech

            for tech in itervalues( self.techGifts ):
                self.logger.log( 'Tech gift: ' + str( count ) + 'x \'' + self.getTechName( tech ) + '\'' )


    def write( self, filename ):
        """
        Write all ROM data back to binary file.

        Keyword arguments:
        filename -- Output file name.
        """

        #If we have a different destination file, create a copy to edit
        if( self.inFilename != filename ):
            copyfile( self.inFilename, filename )

        try:
            file = open( filename, 'r+' + 'b' )
        except IOError:
            self.logger.fatalError( 'Error: output file could not be read (it probably doesn\'t exist)\nMake sure the filename and relative path in settings.ini \'Output\' are correct.' )

        with  file:
            #------------------------------------------------------
            # Write out tech data
            #------------------------------------------------------

            #Pack digimon data into buffer
            data_unpacked = []
            for tech in self.techData:
                data_unpacked.append( tech.unpackedFormat() )

            data_packed = util.packDataArray( data_unpacked, data.techDataFormat )

            #Set all digimon data
            util.writeDataWithExclusions( file,
                                          data_packed,
                                          data.techDataBlockOffset,
                                          data.techDataBlockSize,
                                          data.techDataExclusionOffsets,
                                          data.techDataExclusionSize )


            #------------------------------------------------------
            # Write out digimon data
            #------------------------------------------------------

            #Pack digimon data into buffer
            data_unpacked = []
            for digi in self.digimonData:
                data_unpacked.append( digi.unpackedFormat() )

            data_packed = util.packDataArray( data_unpacked, data.digimonDataFormat )

            #Set all digimon data
            util.writeDataWithExclusions( file,
                                          data_packed,
                                          data.digimonDataBlockOffset,
                                          data.digimonDataBlockSize,
                                          data.digimonDataExclusionOffsets,
                                          data.digimonDataExclusionSize )


            #------------------------------------------------------
            # Write out digimon evo data
            #------------------------------------------------------

            #Pack digimon data into buffer
            data_unpacked = []
            partners = range( 1, data.lastPartnerDigimon + 1 )
            for i, digi in enumerate( self.digimonData ):
                if i in partners:
                    data_unpacked.append( digi.unpackedEvoFormat() )

            data_packed = util.packDataArray( data_unpacked, data.evoToFromFormat )


            #Set all digimon data
            util.writeDataWithExclusions( file,
                                          data_packed,
                                          data.evoToFromBlockOffset,
                                          data.evoToFromBlockSize,
                                          data.evoToFromExclusionOffsets,
                                          data.evoToFromExclusionSize )


            #------------------------------------------------------
            # Write out item data
            #------------------------------------------------------

            #Pack digimon data into buffer
            data_unpacked = []
            for item in self.itemData:
                data_unpacked.append( item.unpackedFormat() )

            data_packed = util.packDataArray( data_unpacked, data.itemDataFormat )

            #Set all digimon data
            util.writeDataWithExclusions( file,
                                          data_packed,
                                          data.itemDataBlockOffset,
                                          data.itemDataBlockSize,
                                          data.itemDataExclusionOffsets,
                                          data.itemDataExclusionSize )


            #------------------------------------------------------
            # Write out starter data
            #------------------------------------------------------

            for i in [ 0, 1 ]:
                #Set digimon ID for starter
                util.writeDataToFile( file,
                                      data.starterSetDigimonOffset[ i ],
                                      struct.pack( data.digimonIDFormat, self.starterID[ i ] ),
                                      self.logger )

                #Set digimon ID to check when learning
                #starter's first tech (must match starter!)
                util.writeDataToFile( file,
                                      data.starterChkDigimonOffset[ i ],
                                      struct.pack( data.digimonIDFormat, self.starterID[ i ] ),
                                      self.logger )

                #Set tech ID for first starter to learn
                util.writeDataToFile( file,
                                      data.starterLearnTechOffset[ i ],
                                      struct.pack( data.techIDFormat, self.starterTech[ i ] ),
                                      self.logger )

                #Set animation ID to equip as first stater's
                #first tech
                util.writeDataToFile( file,
                                      data.starterEquipAnimOffset[ i ],
                                      struct.pack( data.animIDFormat, util.techSlotAnimID( self.starterTechSlot[ i ] ) ),
                                      self.logger )


            #------------------------------------------------------
            # Write out chest item data
            #------------------------------------------------------

            #Set item IDs in chests
            for ofst, item in iteritems( self.chestItems ):
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( data.chestItemFormat, scrutil.spawnChest, item ),
                                      self.logger )

            #------------------------------------------------------
            # Write out map spawn item data
            #------------------------------------------------------

            #Set item spawns in maps
            for ofst, item in iteritems( self.mapItems ):
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( data.mapItemFormat, scrutil.spawnItem, item ),
                                      self.logger )

            #------------------------------------------------------
            # Write out Tokomon item data
            #------------------------------------------------------

            #Set item IDs and counts for Tokomon
            for ofst, ( item, count ) in iteritems( self.tokoItems ):
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( data.tokoItemFormat, scrutil.giveItem, item, count ),
                                      self.logger )

            #------------------------------------------------------
            # Write out Tokomon item data
            #------------------------------------------------------

            #Set check and learn tech for tech gifts
            for ofst, tech in iteritems( self.techGifts ):
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( data.learnMoveFormat, scrutil.learnMove, tech ),
                                      self.logger )

            for i, ofst in enumerate( data.checkMoveOffsets ):
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( data.checkMoveFormat, tech ),
                                      self.logger )



    def randomizeDigimonData( self, dropItem=False, dropRate=False ):
        """
        Randomize digimon data.

        Keyword arguments:
        dropItem -- Randomize dropped item?
        dropRate -- Randomize item drop chance?
        """

        for digi in self.digimonData:
            if( dropItem ):
                digi.item = self._getRandomItem( consumableOnly=True,
                                                             notQuest=True,
                                                             notEvo=True,
                                                             matchValueOf=digi.item )

            if( dropRate ):
                rate = digi.drop_rate

                #Seperately handle 100% drops and never create new 100% drops
                defaultRates = [ 1, 5, 10, 20, 25, 30, 40, 50 ]
                chooseFromRates = [ 1, 1, 1, 5, 10, 20, 25, 30, 40, 50, 50, 50 ]

                #don't change the 100% drops away from being 100%
                if( rate == 0 ):
                    rate = random.choice( defaultRates )
                    digi.drop_rate = newRate
                elif( rate != 100 ):
                    i = defaultRates.index( rate ) + 2
                    newRate = random.choice( chooseFromRates[ i - 2 : i + 3 ] )
                    digi.drop_rate = newRate

            self.logger.logChange( 'Set {:s} to drop {:s} {:d}% of the time'.format( digi.name,
                                                                                     self.getItemName( digi.item ),
                                                                                     digi.drop_rate ) )


    def randomizeStarters( self, useWeakestTech=True ):
        """
        Set starters to two random different rookie Digimon.
        """
        firstDigi = data.rookies[ random.randint( 0, len( data.rookies ) - 1) ]
        secondDigi = firstDigi
        while secondDigi == firstDigi:
            secondDigi = data.rookies[ random.randint( 0, len( data.rookies ) - 1 ) ]

        self.starterID[ 0 ] = firstDigi
        self.logger.logChange( 'First starter set to ' + self.digimonData[ firstDigi ].name )

        self.starterID[ 1 ] = secondDigi
        self.logger.logChange( 'Second starter set to ' + self.digimonData[ secondDigi ].name )

        self._setStarterTechs( useWeakestTech )


    def randomizeChestItems( self, allowEvo=False ):
        """
        Randomize items in chests.

        Keyword arguments:
        allowEvo -- Include or exclude evolution items from
                    the pool of items to choose from.
        """

        #for each chest, choose a random allowed item from data
        for key in list( self.chestItems ):
            randID = self._getRandomItem( notQuest=True, notEvo=( not allowEvo ) )

            pre = self.chestItems[ key ]
            self.chestItems[ key ] = self.itemData[ randID ].id
            self.logger.logChange( 'Changed chest item from ' + self.itemData[ pre ].name + ' to ' + self.itemData[ self.chestItems[ key ] ].name )


    def randomizeTokomonItems( self, consumableOnly=True ):
        """
        Randomize items (and quantity) that Tokomon gives.

        Keyword arguments:
        allowEvo -- Include or exclude evolution items from
                    the pool of items to choose from.
        """

        #for each tokomon item, choose a random allowed item
        #and a random quantity
        for key in list( self.tokoItems ):
            randID = self._getRandomItem( notQuest=True, notEvo=True, consumableOnly=consumableOnly )

            #choose random number 1-3.  Make valuable items less likely
            #to come in large numbers
            randCount = random.randint( 1, 3 )
            if( self.itemData[ randID ].price >= 1000 and randCount > 1 ):
                randCount = random.randint( 1, 3 )
            elif( self.itemData[ randID ].price < 1000 and randCount == 1 ):
                randCount = random.randint( 1, 3 )

            preItem, preCount = self.tokoItems[ key ]
            self.tokoItems[ key ] = ( self.itemData[ randID ].id, randCount )

            self.logger.logChange( 'Changed Tokomon item from ' + str( preCount )  + 'x \'' + self.itemData[ preItem ].name +
                                                         ' to ' + str( randCount ) + 'x \'' + self.itemData[ self.tokoItems[ key ][0] ].name + '\'' )


    def randomizeMapSpawnItems( self, foodOnly=False ):
        """
        Randomize items that appear on maps.  Match value using price.
        If foodOnly is set, replace food items only with other food
        items.

        Keyword arguments:
        foodOnly -- Only replace food items with other food items
        """

        #for each map spawn, choose a random allowed item from data
        for key in list( self.mapItems ):
            id = self.mapItems[ key ]

            #if foodOnly is set, swap food items only for other food items
            fo = foodOnly and self.itemData[ id ].isFood

            randID = self._getRandomItem( foodOnly=fo, consumableOnly=True, notQuest=True, notEvo=True, matchValueOf=id )

            pre = self.mapItems[ key ]
            self.mapItems[ key ] = self.itemData[ randID ].id
            self.logger.logChange( 'Changed map item from ' + self.itemData[ pre ].name + ' to ' + self.itemData[ self.mapItems[ key ] ].name )


    def randomizeEvolutions( self ):
        """
        Randomize the lists of evolutions that each digimon
        is capable of.
        """

        for digi in self.digimonData:
            digi.clearEvos()

        #Freshes each get one in-training target.
        for digi in self.getPlayableDigimonByLevel( data.levelsByName[ 'FRESH' ] ):
            valid = digi.validEvosTo()
            randID = random.randint( 0, len( valid ) - 1 )
            digi.addEvoTo( valid[ randID ].id )

        #In-trainings each get two Rookie targets.
        for digi in self.getPlayableDigimonByLevel( data.levelsByName[ 'IN-TRAINING' ] ):
            digi.updateEvosFrom()
            valid = digi.validEvosTo()
            while( digi.getEvoToCount() < 2 ):
                randID = random.randint( 0, len( valid ) - 1 )
                digi.addEvoTo( valid[ randID ].id )

        #Rookies get 4-6 Champion targets.
        for digi in self.getPlayableDigimonByLevel( data.levelsByName[ 'ROOKIE' ] ):
            count = random.randint( 4, 6 )
            digi.updateEvosFrom()
            valid = digi.validEvosTo()
            while( digi.getEvoToCount() < count ):
                randID = random.randint( 0, len( valid ) - 1 )
                digi.addEvoTo( valid[ randID ].id )

        #Champions get 1-2 Ultimate targets.
        for digi in self.getPlayableDigimonByLevel( data.levelsByName[ 'CHAMPION' ] ):
            count = random.randint( 1, 2 )
            digi.updateEvosFrom()
            valid = digi.validEvosTo()
            while( digi.getEvoToCount() < count ):
                randID = random.randint( 0, len( valid ) - 1 )
                digi.addEvoTo( valid[ randID ].id )

        #Ultimate just need to have their from evos updated.
        for digi in self.getPlayableDigimonByLevel( data.levelsByName[ 'ULTIMATE' ] ):
            digi.updateEvosFrom()

        self.logger.logChange( 'Changed digimon evolutions to the following: ' )
        for i in range( 1, data.lastPartnerDigimon + 1 ):
            self.logger.logChange( 'Changed evolutions for ' + self.digimonData[ i ].evoData() + '\n' )


    def getPlayableDigimonByLevel( self, level ):
        """
        Get a list of digimon with a specified level.

        Keyword arguments:
        level -- Level of digimon to get.
        """

        out = []

        for digi in self.digimonData:
            if( digi.level == level and digi.id in digi.playableDigimon ):
                out.append( digi )

        return out


    def getDigimonName( self, id ):
        """
        Get digimon name from data.

        Keyword arguments:
        id -- Digimon ID to get name for.
        """

        if( id < len( self.digimonData ) ):
            return self.digimonData[ id ].name
        else:
            return '---'


    def getItemName( self, id ):
        """
        Get item name from data.

        Keyword arguments:
        id -- Item ID to get name for.
        """

        if( id < len( self.itemData ) ):
            return self.itemData[ id ].name
        else:
            return 'None'


    def getTechName( self, id ):
        """
        Get tech name from data.

        Keyword arguments:
        id -- Tech ID to get name for.
        """

        if( id < len( data.techs ) ):
            return data.techs[ id ]
        else:
            return 'None'


    def getTypeName( self, id ):
        """
        Get type name from data.

        Keyword arguments:
        id -- Type ID to get name for.
        """

        return util.typeIDToName( id )


    def getSpecialtyName( self, id ):
        """
        Get type name from data.

        Keyword arguments:
        id -- Specialty ID to get name for.
        """

        return util.specIDToName( id )


    def getLevelName( self, id ):
        """
        Get level name from data.

        Keyword arguments:
        id -- Level ID to get name for.
        """

        return util.levelIDToName( id )


    def getRangeName( self, id ):
        """
        Get range name from data.

        Keyword arguments:
        id -- Range ID to get name for.
        """

        if( id in data.ranges ):
            return data.ranges[ id ]
        return "UNDEF"


    def getEffectName( self, id ):
        """
        Get effect name from data.

        Keyword arguments:
        id -- Effect ID to get name for.
        """

        if( id in data.effects ):
            return data.effects[ id ]
        return "NONE"


    def _getRandomItem( self, foodOnly=False, consumableOnly=False, notEvo=False, notQuest=False, matchValueOf=None ):
        """
        Get a random item that satisfies the conditions.

        Keyword arguments:
        foodOnly -- Only allow food items
        consumableOnly -- Only allow consumable items
        notEvo --
        notQuest=False
        matchValueOf=None
        """

        randID = 0
        valid = False
        while( not valid ):
            randID = random.randint( 0, len( self.itemData ) - 1 )
            item = self.itemData[ randID ]
            valid = True

            if( foodOnly and not item.isFood ):
                valid = False

            if( consumableOnly and not item.isConsumable ):
                valid = False

            if( notEvo and item.isEvo ):
                valid = False

            if( notQuest and not item.dropable ):
                valid = False


            if( matchValueOf is not None ):
                itemToMatch = self.itemData[ matchValueOf ]
                if( ( item.price < 1000 ) != ( itemToMatch.price < 1000 ) ):
                    valid = False


        return randID


    def _setStarterTechs( self, useWeakest=True ):
        """
        Set starter techs to either weakest or random.

        Keyword arguments:
        default -- If true, use the lowest tier move available.
                   Otherwise, pick one at random.
        """

        for i in [ 0, 1 ]:
            #Find the lowest tier damaging tech that the digimon
            #can use
            if( useWeakest ):
                lowestTier = 0xFF
                lowestTierID = 0
                for slot, techID in enumerate( self.digimonData[ self.starterID[ i ] ].tech ) :
                    if( self.getTechName( techID ) != 'None' ):
                        tier = self.techData[ techID ].tier
                        if( self.techData[ techID ].isDamaging and not self.techData[ techID ].isFinisher and tier < lowestTier ):
                            lowestTier = tier
                            lowestTierID = techID
                            lowestTierSlot = slot + 1
                self.starterTech[ i ] = lowestTierID
                self.starterTechSlot[ i ] = lowestTierSlot
                self.logger.logChange( 'Starter tech set to ' + self.getTechName( self.starterTech[ i ] )
                                     + ' (' + self.digimonData[ self.starterID[ i ] ].name + '\'s slot ' + str( self.starterTechSlot[ i ] ) + ')' )
            #Select a random learnable damaging tech
            else:
                randID = random.randint( 0, 15 )
                techID = self.digimonData[ self.starterID[ i ] ].tech[ randID ]
                while( self.getTechName( techID ) == 'None' or not self.techData[ techID ].isDamaging or self.techData[ techID ].isFinisher ):
                    randID = random.randint( 0, 15 )
                    techID = self.digimonData[ self.starterID[ i ] ].tech[ randID ]
                self.starterTech[ i ] = techID
                self.starterTechSlot[ i ] = randID + 1
                self.logger.logChange( 'Starter tech set to ' + self.getTechName( self.starterTech[ i ] )
                                     + ' (' + self.digimonData[ self.starterID[ i ] ].name + '\'s slot ' + str( self.starterTechSlot[ i ] ) + ')' )

