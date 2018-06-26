# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Handler that stores all data to be written to the ROM.
"""

import digimon.data as data, digimon.util as util
#import script.util as scrutil
import random, struct
from shutil import copyfile


class DigimonWorldHandler:
    """
    Digimon World handler class.  Holds all data
    that can be modified and written out to the
    file.
    """

    #       Endianness                      Size (packed/not)
    # @     native                              native
    # =     native                              standard
    # <     little-endian                       standard
    # >     big-endian                      standard
    # !     network (= big-endian)  standard

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

    digimonIDFormat = '<B'
    techIDFormat    = '<B'
    animIDFormat    = '<B'
    chestItemFormat = '<BB'

    def __init__( self, filename ):
        """
        Load ROM data into cache so that it can be read
        and manipulated.
        """

        self.inFilename = filename

        with open( filename, 'r' + 'b' ) as file:
            #Read in first starter digimon ID
            file.seek( data.starter1SetDigimonOffset, 0 )
            self.starter1ID = struct.unpack( self.digimonIDFormat, file.read( 1 ) )[0]
            print( data.names[ self.starter1ID ] )

            #Read in first starter learned tech ID
            file.seek( data.starter1LearnTechOffset, 0 )
            self.starter1Tech = struct.unpack( self.techIDFormat, file.read( 1 ) )[0]
            print( '0x' + format( self.starter1Tech, '02x' ) + ' = tech ID' )

            #Read in first starter learned tech slot
            file.seek( data.starter1EquipAnimOffset, 0 )
            self.starter1TechSlot = util.animIDTechSlot( struct.unpack( self.animIDFormat, file.read( 1 ) )[0] )
            print( '0x' + format( self.starter1TechSlot, '02x' ) + ' = tech slot' )

            #Read in second starter ID
            file.seek( data.starter2SetDigimonOffset, 0 )
            self.starter2ID = struct.unpack( self.digimonIDFormat, file.read( 1 ) )[0]
            print( data.names[ self.starter2ID ] )

            #Read in second starter learned tech ID
            file.seek( data.starter2LearnTechOffset, 0 )
            self.starter2Tech = struct.unpack( self.techIDFormat, file.read( 1 ) )[0]
            print( '0x' + format( self.starter2Tech, '02x' ) + ' = tech ID' )

            #Read in second starter learned tech slot
            file.seek( data.starter2EquipAnimOffset, 0 )
            self.starter2TechSlot = util.animIDTechSlot( struct.unpack( self.animIDFormat, file.read( 1 ) )[0] )
            print( '0x' + format( self.starter2TechSlot, '02x' ) + ' = tech slot' )

            self.chestItems = {}

            for ofst in data.chestItemOffsets:
                file.seek( ofst, 0 )
                cmd, item = struct.unpack( self.chestItemFormat, file.read( 2 ) )
                #if( cmd != scrutil.spawnChest ):
                #    print( 'Error: Looking for chest item, found incorrect command: ' + str( cmd ) + ' @ ' + format( ofst, '08x' ) )
                #else:
                self.chestItems[ ofst ] = item

            for item in self.chestItems.values():
                print( 'Chest contains: \'' + data.items[ item ] + '\'' )


    def write( self, filename, verbose=False ):
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
            # Write out first starter data
            #------------------------------------------------------

            #Set digimon ID for first starter
            util.writeDataToFile( file,
                                  data.starter1SetDigimonOffset,
                                  struct.pack( self.digimonIDFormat, self.starter1ID ),
                                  verbose )

            #Set digimon ID to check when learning first
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  data.starter1ChkDigimonOffset,
                                  struct.pack( self.digimonIDFormat, self.starter1ID ),
                                  verbose )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  data.starter1LearnTechOffset,
                                  struct.pack( self.techIDFormat, self.starter1Tech ),
                                  verbose )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  data.starter1EquipAnimOffset,
                                  struct.pack( self.animIDFormat, util.techSlotAnimID( self.starter1TechSlot ) ),
                                  verbose )


            #------------------------------------------------------
            # Write out second starter data
            #------------------------------------------------------

            #Set digimon ID for second starter
            util.writeDataToFile( file,
                                  data.starter2SetDigimonOffset,
                                  struct.pack( self.digimonIDFormat, self.starter2ID ),
                                  verbose )

            #Set digimon ID to check when learning second
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  data.starter2ChkDigimonOffset,
                                  struct.pack( self.digimonIDFormat, self.starter2ID ),
                                  verbose )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  data.starter2LearnTechOffset,
                                  struct.pack( self.techIDFormat, self.starter2Tech ),
                                  verbose )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  data.starter2EquipAnimOffset,
                                  struct.pack( self.animIDFormat, util.techSlotAnimID( self.starter2TechSlot ) ),
                                  verbose )


            #------------------------------------------------------
            # Write out chest item data
            #------------------------------------------------------

            #Set item IDs in chests
            for ofst, item in self.chestItems.iteritems():
                util.writeDataToFile( file,
                                      ofst,
                                      struct.pack( self.chestItemFormat, 0x75, item ),#spawnChest item ),
                                      verbose )


    def randomizeStarters( self ):
        """
        Set starters to two random different rookie Digimon.
        """
        firstDigi = data.rookies[ random.randint( 0, len( data.rookies ) - 1) ]
        secondDigi = firstDigi
        while secondDigi == firstDigi:
            secondDigi = data.rookies[ random.randint( 0, len( data.rookies ) - 1 ) ]

        self.starter1ID = firstDigi
        print( 'First starter set to ' + data.names[ firstDigi ] )

        self.starter2ID = secondDigi
        print( 'Second starter set to ' + data.names[ secondDigi ] )

        self.setStarterTechs( default=True )

    def randomizeChestItems( self, allowEvo=False ):
        """
        Randomize items in chests.

        Keyword arguments:
        allowEvo -- Include or exclude evolution items from
                    the pool of items to choose from.
        """
        #Allow all items besides quest and evolution items
        if( allowEvo ):
            allowedItems = { k:v for k,v in data.items.iteritems() if( k not in data.questItems.keys() ) }
        else:
            allowedItems = { k:v for k,v in data.items.iteritems() if( k not in data.evoItems.keys()
                                                                   and k not in data.questItems.keys() ) }

        for key in self.chestItems.keys():
            pre = self.chestItems[ key ]
            self.chestItems[ key ] = allowedItems.keys()[ random.randint( 0, len( allowedItems ) - 1 ) ]
            print( 'Changed chest item from ' + data.items[ pre ] + ' to ' + data.items[ self.chestItems[ key ] ] )

    def setStarterTechs( self, default=True ):
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
        print( 'First starter tech set to 0x' + format( self.starter1Tech, '02x' ) + ' in slot ' + str( self.starter1TechSlot ) )


        self.starter2Tech = util.starterTech( self.starter2ID )
        self.starter2TechSlot = util.starterTechSlot( self.starter2ID )
        print( 'Second starter tech set to 0x' + format( self.starter2Tech, '02x' ) + ' in slot ' + str( self.starter2TechSlot ) )
