# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

import random
import configparser
import argparse
import sys
from builtins import input
from log.logger import Logger
from digimon.handler import DigimonWorldHandler

#Parse settings argument
args = argparse.ArgumentParser( description='Randomize Digimon World' )
args.add_argument( '-settings', required=True, help='Settings INI file to use to configure the randomization.' )
settings = args.parse_args( sys.argv[1:] ).settings

#Load settings from specified file
if( settings == '' ):
    print( 'Settings file must be provided at command line.  Use [-h] for help.' )
    exit()
config = configparser.ConfigParser( allow_no_value=True )
config.read( settings )

verbose = config[ 'general' ][ 'LogLevel' ]
logger = Logger( verbose, filename='randomize.log' )

if( config[ 'general' ][ 'Input' ] != '' ):
    inFile = config[ 'general' ][ 'Input' ]
else:
    logger.fatalError( 'Must provide file name in settings "Input".' )
    exit()

#If an output file was Set, use that as the output.
#Otherwise, read and write the same file
if( config[ 'general' ][ 'Output' ] != '' ):
    outFile = config[ 'general' ][ 'Output' ]
else:
    outFile = inFile

#Give the user a warning when we are going to overwrite the base ROM
#if( outFile == inFile ):
#    qa = input( 'Warning: currently set to overwrite the input file.\nAre you sure you want to continue? (y/n)' )
#    if( qa != 'y' ):
#        print( 'Exiting.  Please update settings.ini \'Output\' to select a different output location.' )
#        exit()

print( 'Reading data from ' + inFile + '...' )
sys.stdout.flush()

seedcfg = config[ 'general' ][ 'Seed' ]

if( seedcfg == '' ):
    handler = DigimonWorldHandler( inFile, logger )
else:
    try:
        handler = DigimonWorldHandler( inFile, logger, seed=int( seedcfg ) )
    except ValueError:
        logger.fatalError( 'Seed must be an integer. ' + str( seedcfg ) + ' is not a valid value.' )

print( 'Modifying data...' )
sys.stdout.flush()

if( config[ 'digimon' ].getboolean( 'Enabled' ) ):
    pricecfg =  config[ 'digimon' ][ 'ValuableItemCutoff' ]
    try:
        handler.randomizeDigimonData( dropItem=config[ 'digimon' ].getboolean( 'DropItem' ),
                                      dropRate=config[ 'digimon' ].getboolean( 'DropRate' ),
                                      price=int( pricecfg ) )
    except ValueError:
        logger.fatalError( 'Item price cutoff must be an integer. ' + str( seedcfg ) + ' is not a valid value.' )

if( config[ 'techs' ].getboolean( 'Enabled' ) ):
    handler.randomizeTechData( power=config[ 'techs' ].getboolean( 'Power' ),
                               mode=config[ 'techs' ][ 'mode' ],
                               cost=config[ 'techs' ].getboolean( 'Cost' ),
                               accuracy=config[ 'techs' ].getboolean( 'Accuracy' ),
                               effect=config[ 'techs' ].getboolean( 'Effect' ),
                               effectChance=config[ 'techs' ].getboolean( 'EffectChance' ) )

if( config[ 'starter' ].getboolean( 'Enabled' ) ):
    handler.randomizeStarters( useWeakestTech=config[ 'starter' ].getboolean( 'UseWeakestTech' ) )

if( config[ 'recruitment' ].getboolean( 'Enabled' ) ):
    handler.randomizeRecruitments()

if( config[ 'chests' ].getboolean( 'Enabled' ) ):
    handler.randomizeChestItems( allowEvo=config[ 'chests' ].getboolean( 'AllowEvo' ) )

if( config[ 'tokomon' ].getboolean( 'Enabled' ) ):
    handler.randomizeTokomonItems( consumableOnly=config[ 'tokomon' ].getboolean( 'ConsumableOnly' ) )

if( config[ 'techgifts' ].getboolean( 'Enabled' ) ):
    handler.randomizeTechGifts()

if( config[ 'mapItems' ].getboolean( 'Enabled' ) ):
    pricecfg =  config[ 'mapItems' ][ 'ValuableItemCutoff' ]
    try:
        handler.randomizeMapSpawnItems( foodOnly=config[ 'mapItems' ].getboolean( 'FoodOnly' ), price=int( pricecfg ) )
    except ValueError:
        logger.fatalError( 'Item price cutoff must be an integer. ' + str( seedcfg ) + ' is not a valid value.' )

if( config[ 'evolution' ].getboolean( 'Enabled' ) ):
    if( config[ 'evolution' ].getboolean( 'Requirements' ) ):
        handler.randomizeEvolutionRequirements()
    handler.randomizeEvolutions( obtainAll=config[ 'evolution' ].getboolean( 'ObtainAll' ) )
    if( config[ 'evolution' ].getboolean( 'SpecialEvos' ) ):
        handler.randomizeSpecialEvolutions()
        handler.updateEvolutionStats()

if( config[ 'patches' ].getboolean( 'FixEvoItemStatGain' ) ):
    handler.applyPatch( 'fixEvoItems' )

if( config[ 'patches' ].getboolean( 'AllowDropQuestItems' ) ):
    handler.applyPatch( 'allowDrop' )

if( config[ 'patches' ].getboolean( 'Woah' ) ):
    handler.applyPatch( 'woah' )

if( config[ 'patches' ].getboolean( 'FixBrainTrainTierOne' ) ):
    handler.applyPatch( 'learnTierOne' )

if( config[ 'patches' ].getboolean( 'FixGiromonJukeboxGlitch' ) ):
    handler.applyPatch( 'giromon' )

if( config[ 'patches' ].getboolean( 'IncreaseTechLearnChance' ) ):
    handler.applyPatch( 'upLearnChance' )

if( config[ 'patches' ].getboolean( 'Gabu' ) ):
    handler.applyPatch( 'gabumon' )
    
if( config[ 'patches' ][ 'SetSpawnRate' ] != '' ):
    handler.applyPatch( 'spawn', int( config[ 'patches' ][ 'SetSpawnRate' ] ) )
    
if( config[ 'patches' ].getboolean( 'ShowHashIntro' ) ):
    handler.applyPatch( 'hash', config[ 'general' ][ 'Hash '] )


print( 'Writing to ' + outFile + '...' )
sys.stdout.flush()
handler.write( outFile )

if( not logger.error ):
    print( 'Modifications completed successfully.  See log file for details (Warning: spoilers!).' )
    print( 'Seed was ' + str( handler.randomseed ) )
    print( 'Enter this seed in settings file to produce the same ROM again.' )
else:
    print( 'Program ended with errors.  See log file for details.' )
sys.stdout.flush()

logger.logAlways( logger.getHeader( 'Seed' ) )

logger.logAlways( 'Seed was ' + str( handler.randomseed ) + '.' )

logger.logAlways( logger.getHeader( 'End of log' ) )
