# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Handler that stores all data to be written to the ROM.
"""

import data, util
import random
from shutil import copyfile

class DigimonWorldHandler:
    """
    Digimon World handler class.  Holds all data
    that can be modified and written out to the
    file.
    """

    def __init__( self, file ):
        """
        Load ROM data into cache so that it can be read
        and manipulated.
        """

        self.inFilename = filename

        with open( filename, 'r' + 'b' ) as file:
            #Read in first starter digimon ID
            file.seek( data.starter1SetDigimonOffset, 0 )
            self.starter1ID = int.from_bytes( file.read( 1 ), byteorder='little' )

            #Read in first starter learned tech ID
            file.seek( data.starter1LearnTechOffset, 0 )
            self.starter1Tech = int.from_bytes( file.read( 1 ), byteorder='little' )

            #Read in first starter learned tech slot
            file.seek( data.starter1EquipAnimOffset, 0 )
            self.starter1TechSlot = util.animIDTechSlot( int.from_bytes( file.read( 1 ), byteorder='little' ) )

            #Read in second starter ID
            file.seek( data.starter2SetDigimonOffset, 0 )
            self.starter2ID = int.from_bytes( file.read( 1 ), byteorder='little' )

            #Read in second starter learned tech ID
            file.seek( data.starter2LearnTechOffset, 0 )
            self.starter2Tech = int.from_bytes( file.read( 1 ), byteorder='little' )

            #Read in second starter learned tech slot
            file.seek( data.starter2EquipAnimOffset, 0 )
            self.starter2TechSlot = util.animIDTechSlot( int.from_bytes( file.read( 1 ), byteorder='little' ) )


    def write( self, filename ):
        copyfile( self.inFilename, filename )

        with open( filename, 'r+' + 'b' ) as file:
            #------------------------------------------------------
            # Write out first starter data
            #------------------------------------------------------

            #Set digimon ID for first starter
            util.writeDataToFile( file,
                                  data.starter1SetDigimonOffset,
                                  0,
                                  self.starter1ID )

            #Set digimon ID to check when learning first
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  starter1ChkDigimonOffset,
                                  0,
                                  self.starter1ID )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  starter1LearnTechOffset,
                                  0,
                                  self.starter1Tech )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  starter1EquipAnimOffset,
                                  0,
                                  util.techSlotAnimID( self.starter1TechSlot ) )

            #------------------------------------------------------
            # Write out second starter data
            #------------------------------------------------------

            #Set digimon ID for second starter
            util.writeDataToFile( file,
                                  data.starter2SetDigimonOffset,
                                  0,
                                  self.starter2ID )

            #Set digimon ID to check when learning second
            #starter's first tech (must match starter!)
            util.writeDataToFile( file,
                                  starter2ChkDigimonOffset,
                                  0,
                                  self.starter2ID )

            #Set tech ID for first starter to learn
            util.writeDataToFile( file,
                                  starter2LearnTechOffset,
                                  0,
                                  self.starter2Tech )

            #Set animation ID to equip as first stater's
            #first tech
            util.writeDataToFile( file,
                                  starter2EquipAnimOffset,
                                  0,
                                  util.techSlotAnimID( self.starter2TechSlot ) )


    def randomizeStarters( self ):
        """
        Set starters to two random different rookie Digimon.
        """
        firstDigi = rookies[random.randint(0, len(rookies) - 1)]
        secondDigi = firstDigi
        while secondDigi == firstDigi:
            secondDigi = rookies[random.randint(0, len(rookies) - 1)]

        self.starter1ID = firstDigi
        self.starter2ID = secondDigi


    def updateStarterTechs( self ):
        """
        Set starter techs to default techs (lowest tier tech
        learnable by default) for current starters.
        """
        self.starter1Tech = util.starterTech( starter1ID )
        self.starter1TechSlot = util.starterTechSlot( starter1ID )

        self.starter2Tech = util.starterTech( starter2ID )
        self.starter2TechSlot = util.starterTechSlot( starter2ID )

