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
    playableDigimon = list( range( 0x00, 0x3E ) ) + [ 0x3F, 40, 41 ]


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

        out = self.name + '\nEvolves from '

        for i in range( 5 ):
            out += self.handler.getDigimonName( self.fromEvo[ i ] ) + ' '

        out += '\nEvolves to '

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


    def updateEvosFrom( self ):
        """
        Update this digimon's list of digimon that
        can evolve into it.
        """

        evos = []
        for digi in self.handler.digimonData:
            if( self.id in digi.evosTo ):
                evos.append( digi.id )
                
        #This is the order in which evos are filled
        #i.e. if there are two evos, they are in
        #the 3rd slot and the 2nd slot (#2, #1)
        #Copy up to 5 evos in.  If less, fill with
        #0xFF, aka none.  Truncate extras.
        for i, j in enumerate( [ 2, 1, 3, 0, 4 ] ):
            if( i < len( evos ) ):
                evosFrom[ j ] = evos[ i ]
            else:
                evosFrom[ j ] = 0xFF
                
                
    def validEvosTo( self ):
        """
        Produce list of valid digimon IDs that this 
        digimon could potentially evolve to.
        """
        
        evos = []
        
        #Find all digimon that are playable and one level above
        for digi in self.handler.digimonData:
            if( digi.id in playableDigimon and digi.level == self.level + 1 ):
                evos.append( digi.id )
        
        return evos


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


    def isAllowedInChest( self, allowEvos ):
        """
        Check if this item should be allowed in chests,
        allowing or disallowing evos as necessary.  Always
        ban quest items (undroppable).
        """

        if( allowEvos ):
            return self.dropable
        else:
            return ( self.dropable and not self.isEvo )


    def isAllowedTokomon( self, onlyConsumables ):
        """
        Check if this item should be allowed for Tokomon.
        Always ban quest items and evos (game breaking).
        Restrict to consumables if needed.
        """

        if( onlyConsumables ):
            return ( self.isConsumable and not self.isEvo )
        else:
            return ( self.dropable and not self.isEvo )


    def isAllowedMap( self, onlyFood, lowValue ):
        """
        Check if this item should be allowed to spawn on the
        map.  Always ban quest items and evos (game breaking).
        """

        ret = False

        if( onlyFood ):
            ret = self.isFood
        else:
            ret = ( self.isConsumable and not self.isEvo )

        if( lowValue and self.price < 1000 ):
            return ret
        elif( not lowValue and self.price >= 1000 ):
            return ret
        else:
            return False


class Tech:
    """
    Tech data object.  Stores all data about a given
    tech.  Currently only names (read ONLY)
    """

    def __init__( self, handler, id, data ):
        """
        Separate out composite data into individual
        components.

        Keyword arguments:
        data -- List of values (unpacked from data string).
        """

        self.handler  = handler
        self.id       = id

        self.name     = data[ 0 ]



    def __str__( self ):
        """
        Produce a string representation of the object
        for convenient logging.
        """

        return self.name


    def unpackedFormat( self ):
        """
        Produce a tuple representation of all
        of the data in the object.
        """
        repr = []

        #convert to binary, add null terminator, and pad to 4 bytes
        name = self.name.encode( 'ascii' ) + b'\00'
        while( len( name ) % 4 != 0 ):
            name += b'\00'

        repr.append( self.name )

        return tuple( repr )


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

        with open( filename, 'r' + 'b' ) as file:
            #------------------------------------------------------
            # Read in tech name data
            #------------------------------------------------------

            #Read in full tech name data block
            data_read = util.readDataWithExclusions( file,
                                                     data.techNameBlockOffset,
                                                     data.techNameBlockSize,
                                                     data.techNameExclusionOffsets,
                                                     data.techNameExclusionSize )

            data_unpacked = list( filter( None, data_read.decode( 'ascii' ).split( '\0' ) ) )

            self.techData = []
            for i, name in enumerate( data_unpacked ):
                self.techData.append( Tech( self, i, ( name, ) ) )
                self.logger.log( str( self.techData[ i ] ) )


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
            # Read in first starter data
            #------------------------------------------------------

            #Read in first starter digimon ID
            file.seek( data.starter1SetDigimonOffset, 0 )
            self.starter1ID = struct.unpack( data.digimonIDFormat, file.read( 1 ) )[0]
            self.logger.log( self.digimonData[ self.starter1ID ].name )

            #Read in first starter learned tech ID
            file.seek( data.starter1LearnTechOffset, 0 )
            self.starter1Tech = struct.unpack( data.techIDFormat, file.read( 1 ) )[0]
            self.logger.log( '0x' + format( self.starter1Tech, '02x' ) + ' = tech ID' )

            #Read in first starter learned tech slot
            file.seek( data.starter1EquipAnimOffset, 0 )
            self.starter1TechSlot = util.animIDTechSlot( struct.unpack( data.animIDFormat, file.read( 1 ) )[0] )
            self.logger.log( '0x' + format( self.starter1TechSlot, '02x' ) + ' = tech slot' )


            #------------------------------------------------------
            # Read in first starter data
            #------------------------------------------------------

            #Read in second starter ID
            file.seek( data.starter2SetDigimonOffset, 0 )
            self.starter2ID = struct.unpack( data.digimonIDFormat, file.read( 1 ) )[0]
            self.logger.log( self.digimonData[ self.starter2ID ].name )

            #Read in second starter learned tech ID
            file.seek( data.starter2LearnTechOffset, 0 )
            self.starter2Tech = struct.unpack( data.techIDFormat, file.read( 1 ) )[0]
            self.logger.log( '0x' + format( self.starter2Tech, '02x' ) + ' = tech ID' )

            #Read in second starter learned tech slot
            file.seek( data.starter2EquipAnimOffset, 0 )
            self.starter2TechSlot = util.animIDTechSlot( struct.unpack( data.animIDFormat, file.read( 1 ) )[0] )
            self.logger.log( '0x' + format( self.starter2TechSlot, '02x' ) + ' = tech slot' )


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


    def write( self, filename ):
        """
        Write all ROM data back to binary file.

        Keyword arguments:
        filename -- Output file name.
        """

        #If we have a different destination file, create a copy to edit
        if( self.inFilename != filename ):
            copyfile( self.inFilename, filename )

        with open( filename, 'r+' + 'b' ) as file:
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
            # Write out first starter data
            #------------------------------------------------------

            #Set digimon ID for first starter
            util.writeDataToFile( file,
                                  data.starter1SetDigimonOffset,
                                  struct.pack( data.digimonIDFormat, self.starter1ID ),
                                  self.logger.verbose )

            #Set digimon ID to check when learning first
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  data.starter1ChkDigimonOffset,
                                  struct.pack( data.digimonIDFormat, self.starter1ID ),
                                  self.logger.verbose )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  data.starter1LearnTechOffset,
                                  struct.pack( data.techIDFormat, self.starter1Tech ),
                                  self.logger.verbose )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  data.starter1EquipAnimOffset,
                                  struct.pack( data.animIDFormat, util.techSlotAnimID( self.starter1TechSlot ) ),
                                  self.logger.verbose )


            #------------------------------------------------------
            # Write out second starter data
            #------------------------------------------------------

            #Set digimon ID for second starter
            util.writeDataToFile( file,
                                  data.starter2SetDigimonOffset,
                                  struct.pack( data.digimonIDFormat, self.starter2ID ),
                                  self.logger.verbose )

            #Set digimon ID to check when learning second
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  data.starter2ChkDigimonOffset,
                                  struct.pack( data.digimonIDFormat, self.starter2ID ),
                                  self.logger.verbose )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  data.starter2LearnTechOffset,
                                  struct.pack( data.techIDFormat, self.starter2Tech ),
                                  self.logger.verbose )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  data.starter2EquipAnimOffset,
                                  struct.pack( data.animIDFormat, util.techSlotAnimID( self.starter2TechSlot ) ),
                                  self.logger.verbose )


            #------------------------------------------------------
            # Write out chest item data
            #------------------------------------------------------

            #Set item IDs in chests
            for ofst, item in iteritems( self.chestItems ):
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( data.chestItemFormat, scrutil.spawnChest, item ),
                                      self.logger.verbose )

            #------------------------------------------------------
            # Write out map spawn item data
            #------------------------------------------------------

            #Set item spawns in maps
            for ofst, item in iteritems( self.mapItems ):
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( data.mapItemFormat, scrutil.spawnItem, item ),
                                      self.logger.verbose )

            #------------------------------------------------------
            # Write out Tokomon item data
            #------------------------------------------------------

            #Set item IDs and counts for Tokomon
            for ofst, ( item, count ) in iteritems( self.tokoItems ):
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( data.tokoItemFormat, scrutil.giveItem, item, count ),
                                      self.logger.verbose )


    def randomizeStarters( self, useWeakestTech=True ):
        """
        Set starters to two random different rookie Digimon.
        """
        firstDigi = data.rookies[ random.randint( 0, len( data.rookies ) - 1) ]
        secondDigi = firstDigi
        while secondDigi == firstDigi:
            secondDigi = data.rookies[ random.randint( 0, len( data.rookies ) - 1 ) ]

        self.starter1ID = firstDigi
        self.logger.log( 'First starter set to ' + self.digimonData[ firstDigi ].name )

        self.starter2ID = secondDigi
        self.logger.log( 'Second starter set to ' + self.digimonData[ secondDigi ].name )

        self._setStarterTechs( default=useWeakestTech )


    def randomizeChestItems( self, allowEvo=False ):
        """
        Randomize items in chests.

        Keyword arguments:
        allowEvo -- Include or exclude evolution items from
                    the pool of items to choose from.
        """

        #for each chest, choose a random allowed item from data
        for key in list( self.chestItems ):
            randID = random.randint( 0, len( self.itemData ) - 1 )
            while( not self.itemData[ randID ].isAllowedInChest( allowEvo ) ):
                randID = random.randint( 0, len( self.itemData ) - 1 )

            pre = self.chestItems[ key ]
            self.chestItems[ key ] = self.itemData[ randID ].id
            self.logger.log( 'Changed chest item from ' + self.itemData[ pre ].name + ' to ' + self.itemData[ self.chestItems[ key ] ].name )


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
            randID = random.randint( 0, len( self.itemData ) - 1 )
            while( not self.itemData[ randID ].isAllowedTokomon( consumableOnly ) ):
                randID = random.randint( 0, len( self.itemData ) - 1 )

            #choose random number 1-3.  Make valuable items less likely
            #to come in large numbers
            randCount = random.randint( 1, 3 )
            if( self.itemData[ randID ].price >= 1000 and randCount > 1 ):
                randCount = random.randint( 1, 3 )
            elif( self.itemData[ randID ].price < 1000 and randCount == 1 ):
                randCount = random.randint( 1, 3 )

            preItem, preCount = self.tokoItems[ key ]
            self.tokoItems[ key ] = ( self.itemData[ randID ].id, randCount )

            self.logger.log( 'Changed Tokomon item from ' + str( preCount ) + 'x \'' + self.itemData[ preItem ].name +
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
            #if foodOnly is set, swap food items only for other food items
            fo = foodOnly and self.itemData[ self.mapItems[ key ] ].isFood

            #match low-val and high-val items with similar to keep %
            #reasonable
            lowVal = self.itemData[ self.mapItems[ key ] ].price < 1000

            randID = random.randint( 0, len( self.itemData ) - 1 )
            while( not self.itemData[ randID ].isAllowedMap( fo, lowVal ) ):
                randID = random.randint( 0, len( self.itemData ) - 1 )

            pre = self.mapItems[ key ]
            self.mapItems[ key ] = self.itemData[ randID ].id
            self.logger.log( 'Changed map item from ' + self.itemData[ pre ].name + ' to ' + self.itemData[ self.mapItems[ key ] ].name )


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

        if( id < len( self.techData ) ):
            return self.techData[ id ].name
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


    def _setStarterTechs( self, default=True ):
        """
        Set starter techs to default techs (lowest tier tech
        learnable by default) for current starters.

        Keyword arguments:
        default -- No handling for now.  Support to be added
                   for other options (random) but that is
                   not possible now.
        """
        self.starter1Tech = util.starterTech( self.starter1ID )
        self.starter1TechSlot = util.starterTechSlot( self.starter1ID )
        self.logger.log( 'First starter tech set to ' + self.getTechName( self.starter1Tech )
             + ' (' + self.digimonData[ self.starter1ID ].name + '\'s slot ' + str( self.starter1TechSlot ) + ')' )


        self.starter2Tech = util.starterTech( self.starter2ID )
        self.starter2TechSlot = util.starterTechSlot( self.starter2ID )
        self.logger.log( 'Second starter tech set to ' + self.getTechName( self.starter2Tech )
             + ' (' + self.digimonData[ self.starter2ID ].name + '\'s slot ' + str( self.starter2TechSlot ) + ')' )

