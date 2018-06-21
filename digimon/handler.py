# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Handler that stores all data to be written to the ROM.
"""

import data, util
import random, struct
from shutil import copyfile

class DigimonWorldHandler:
    """
    Digimon World handler class.  Holds all data
    that can be modified and written out to the
    file.
    """

    #       Endianness              Size (packed/not)
    # @ 	native 	                native
    # = 	native 	                standard
    # < 	little-endian 	        standard
    # > 	big-endian 	            standard
    # ! 	network (= big-endian) 	standard

    #       Type
    # x 	pad byte
    # c 	char
    # b 	signed char
    # B 	unsigned char
    # ? 	_Bool
    # h 	short
    # H 	unsigned short
    # i 	int
    # I 	unsigned int
    # l 	long
    # L 	unsigned long
    # q 	long long
    # Q 	unsigned long long
    # f 	float
    # d 	double
    # s 	char[]
    # p 	char[]
    # P 	void *

    digimonIDFormat = "=B"
    techIDFormat    = "=B"
    animIDFormat    = "=B"

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
            print( '0x' + format( self.starter1ID, '02x' ) + ' = starter ID')

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
            print( '0x' + format( self.starter2ID, '02x' ) + ' = starter ID' )

            #Read in second starter learned tech ID
            file.seek( data.starter2LearnTechOffset, 0 )
            self.starter2Tech = struct.unpack( self.techIDFormat, file.read( 1 ) )[0]
            print( '0x' + format( self.starter2Tech, '02x' ) + ' = tech ID' )

            #Read in second starter learned tech slot
            file.seek( data.starter2EquipAnimOffset, 0 )
            self.starter2TechSlot = util.animIDTechSlot( struct.unpack( self.animIDFormat, file.read( 1 ) )[0] )
            print( '0x' + format( self.starter2TechSlot, '02x' ) + ' = tech slot' )


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
                                  0,
                                  struct.pack( self.digimonIDFormat, self.starter1ID ),
                                  verbose )

            #Set digimon ID to check when learning first
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  data.starter1ChkDigimonOffset,
                                  0,
                                  struct.pack( self.digimonIDFormat, self.starter1ID ),
                                  verbose )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  data.starter1LearnTechOffset,
                                  0,
                                  struct.pack( self.techIDFormat, self.starter1Tech ),
                                  verbose )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  data.starter1EquipAnimOffset,
                                  0,
                                  struct.pack( self.animIDFormat, util.techSlotAnimID( self.starter1TechSlot ) ),
                                  verbose )

            #------------------------------------------------------
            # Write out second starter data
            #------------------------------------------------------

            #Set digimon ID for second starter
            util.writeDataToFile( file,
                                  data.starter2SetDigimonOffset,
                                  0,
                                  struct.pack( self.digimonIDFormat, self.starter2ID ),
                                  verbose )

            #Set digimon ID to check when learning second
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  data.starter2ChkDigimonOffset,
                                  0,
                                  struct.pack( self.digimonIDFormat, self.starter2ID ),
                                  verbose )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  data.starter2LearnTechOffset,
                                  0,
                                  struct.pack( self.techIDFormat, self.starter2Tech ),
                                  verbose )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  data.starter2EquipAnimOffset,
                                  0,
                                  struct.pack( self.animIDFormat, util.techSlotAnimID( self.starter2TechSlot ) ),
                                  verbose )


    def randomizeStarters( self ):
        """
        Set starters to two random different rookie Digimon.
        """
        firstDigi = data.rookies[random.randint(0, len(data.rookies) - 1)]
        secondDigi = firstDigi
        while secondDigi == firstDigi:
            secondDigi = data.rookies[random.randint(0, len(data.rookies) - 1)]

        self.starter1ID = firstDigi
        print( 'First starter set to 0x' + format( firstDigi, '02x' ) )

        self.starter2ID = secondDigi
        print( 'Second starter set to 0x' + format( secondDigi, '02x' ) )


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
        print( 'First starter tech set to 0x' + format( self.starter2Tech, '02x' ) + ' in slot ' + str( self.starter2TechSlot ) )
