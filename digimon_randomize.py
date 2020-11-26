# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

import random
import argparse
import json
from json import JSONDecodeError
import sys
from builtins import input
from digimon.data import levels
from log.logger import Logger
from digimon.handler import DigimonWorldHandler

#Parse settings argument
args = argparse.ArgumentParser( description='Randomize Digimon World' )
args.add_argument( '-settings', required=True, help='JSON settings string that configures the operation' )
settings = args.parse_args( sys.argv[1:] ).settings

#Load settings from specified file
if( settings == '' ):
    print( 'Settings file must be provided at command line.  Use [-h] for help.' )
    exit()

config = {}
try:
    config = json.loads( settings )
except JSONDecodeError as err:
    print( "Failed to parse JSON" )
    print( err )
    exit()

verbose = config[ 'general' ][ 'LogLevel' ]

if( config[ 'general' ][ 'InputFile' ] != '' ):
    inFile = config[ 'general' ][ 'InputFile' ]
else:
    print( 'ROM file section is required' )
    exit()

#If an output file was Set, use that as the output.
#Otherwise, read and write the same file
if( config[ 'general' ][ 'OutputFile' ] != '' ):
    outFile = config[ 'general' ][ 'OutputFile' ]
else:
    print( 'Destination file section is required' )
    exit

print( 'Reading data from ' + inFile + '...' )
sys.stdout.flush()

try:
    seedcfg = config[ 'general' ][ 'Seed' ]
    name = 'randomize.log'
    logger = Logger( verbose, filename=name )
    handler = DigimonWorldHandler( inFile, logger, seed=int( seedcfg ) )
except ValueError:
    print( 'Seed must be an integer. ' + str( seedcfg ) + ' is not a valid value.' )
    exit()
except Exception as e:
    print( e )
    logger = Logger( verbose, filename='randomize.log' )
    handler = DigimonWorldHandler( inFile, logger )

print( 'Modifying data...' )
sys.stdout.flush()

if( config[ 'digimon' ][ 'Enabled' ] ):
    if( config[ 'digimon' ][ 'MatchValue' ] ):
        pricecfg =  config[ 'digimon' ][ 'ValuableItemCutoff' ]
    else:
        pricecfg = "10000"
    try:
        handler.randomizeDigimonData( dropItem=config[ 'digimon' ][ 'DroppedItem' ],
                                      dropRate=config[ 'digimon' ][ 'DropRate' ],
                                      price=int( pricecfg ) )
    except ValueError:
        logger.fatalError( 'Item price cutoff must be an integer. ' + str( pricecfg ) + ' is not a valid value.' )

if( config[ 'techs' ][ 'Enabled' ] ):
    handler.randomizeTechData( power=config[ 'techs' ][ 'Power' ],
                               mode=config[ 'techs' ][ 'RandomizationMode' ],
                               cost=config[ 'techs' ][ 'Cost' ],
                               accuracy=config[ 'techs' ][ 'Accuracy' ],
                               effect=config[ 'techs' ][ 'Effect' ],
                               effectChance=config[ 'techs' ][ 'EffectChance' ] )
    
    if( config[ 'techs' ][ 'TypeEffectiveness']):
        handler.applyPatch( 'typeEffectiveness' )

if( config[ 'starter' ][ 'Enabled' ] ):
    #Use true/false values as a mask against the list of levels
    #to get a list of levels that are enabled
    levelsMask = [ 
        config[ 'starter' ][ 'Fresh' ], 
        config[ 'starter' ][ 'InTraining' ],
        config[ 'starter' ][ 'Rookie' ],
        config[ 'starter' ][ 'Champion' ],
        config[ 'starter' ][ 'Ultimate' ]
    ]
    levelValues = list( levels.keys() )

    handler.randomizeStarters( 
        useWeakestTech=config[ 'starter' ][ 'UseWeakestTech' ],
        forceDigimon=config[ 'starter' ][ 'Digimon' ],
        allowedLevels=[ b for a, b in zip( levelsMask, levelValues ) if a ]
    )

if( config[ 'recruitment' ][ 'Enabled' ] ):
    handler.randomizeRecruitments()

if( config[ 'chests' ][ 'Enabled' ] ):
    handler.randomizeChestItems( allowEvo=config[ 'chests' ][ 'AllowEvolutionItems' ] )

if( config[ 'tokomon' ][ 'Enabled' ] ):
    handler.randomizeTokomonItems( consumableOnly=config[ 'tokomon' ][ 'ConsumableOnly' ] )

if( config[ 'techGifts' ][ 'Enabled' ] ):
    handler.randomizeTechGifts()

if( config[ 'mapItems' ][ 'Enabled' ] ):
    if( config[ 'mapItems' ][ 'MatchValue' ] ):
        pricecfg = config[ 'mapItems' ][ 'ValuableItemCutoff' ]
    else:
        pricecfg = "10000"
    try:
        handler.randomizeMapSpawnItems( foodOnly=config[ 'mapItems' ][ 'FoodOnly' ], price=int( pricecfg ) )
    except ValueError:
        logger.fatalError( 'Item price cutoff must be an integer. ' + str( pricecfg ) + ' is not a valid value.' )

if( config[ 'evolution' ][ 'Enabled' ] ):
    if( config[ 'evolution' ][ 'Requirements' ] ):
        handler.randomizeEvolutionRequirements()
    handler.randomizeEvolutions( obtainAll=config[ 'evolution' ][ 'ObtainAllMode' ] )
    if( config[ 'evolution' ][ 'SpecialEvolutions' ] ):
        handler.randomizeSpecialEvolutions()
        handler.updateEvolutionStats()

if( config[ 'patches' ][ 'Enabled' ] ):
    if( config[ 'patches' ][ 'EvoItemStatGain' ] ):
        handler.applyPatch( 'fixEvoItems' )

    if( config[ 'patches' ][ 'QuestItemsDroppable' ] ):
        handler.applyPatch( 'allowDrop' )

    if( config[ 'patches' ][ 'Woah' ] ):
        handler.applyPatch( 'woah' )

    if( config[ 'patches' ][ 'BrainTrainTierOne' ] ):
        handler.applyPatch( 'learnTierOne' )

    if( config[ 'patches' ][ 'JukeboxGlitch' ] ):
        handler.applyPatch( 'giromon' )

    if( config[ 'patches' ][ 'IncreaseLearnChance' ] ):
        handler.applyPatch( 'upLearnChance' )

    if( config[ 'patches' ][ 'Gabu' ] ):
        handler.applyPatch( 'gabumon' )
        
    if( config[ 'patches' ][ 'SpawnRateEnabled' ] != '0' ):
        handler.applyPatch( 'spawn', int( config[ 'patches' ][ 'SpawnRate' ] ) )
        
    if( config[ 'patches' ][ 'ShowHashIntro' ] ):
        handler.applyPatch( 'hash', config[ 'general' ][ 'Hash'] )
        
    if( config[ 'patches' ][ 'SkipIntro' ] ):
        handler.applyPatch( 'intro' )

    if( config[ 'patches' ][ 'UnlockAreas' ] ):
        handler.applyPatch( 'unlock' )

    if( config[ 'patches' ][ 'UnrigSlots' ] ):
        handler.applyPatch( 'slots' )

    if( config[ 'patches' ][ 'Softlock' ] ):
        handler.applyPatch( 'softlock' )
        
    if( config[ 'patches' ][ 'LearnMoveAndCommand' ] ):
        handler.applyPatch( 'learnmoveandcommand' )

    if( config[ 'patches' ][ 'FixDVChips' ] ):
        handler.applyPatch( 'fixDVChips' )

    if( config[ 'patches' ][ 'HappyVending' ] ):
        handler.applyPatch( 'happyVending' )

print( 'Writing to ' + outFile + '...' )
sys.stdout.flush()

try:
    handler.write( outFile )
except Exception as ex:
    logger.logError( 'System error: {0}'.format(ex) )
    print( 'An irrecoverable error occured' )

if( not logger.error ):
    print( 'Modifications completed successfully.  See log file for details (Warning: spoilers!).' )
    print( 'Seed was ' + str( handler.randomseed ) )
    print( 'Enter this seed in settings file to produce the same ROM again.' )
else:
    print( 'Program ended with errors.  See log file for details.' )
sys.stdout.flush()

logger.logAlways( logger.getHeader( 'Seed' ) )

logger.logAlways( 'Seed was ' + str( handler.randomseed ) + '.' )

logger.close()

logger.rename( 'randomize-' + str( handler.randomseed ) + '.log')
