# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

import random
import configparser
import sys
from log.logger import Logger
from digimon.handler import DigimonWorldHandler

config = configparser.ConfigParser( allow_no_value=True )
config.read( 'settings.ini' )

verbose = config[ 'general' ][ 'LogLevel' ]
logger = Logger( verbose, filename='randomize.log' )

if( len(sys.argv) > 1 ):
    input = sys.argv[1]
elif( config[ 'general' ][ 'Input' ] != '' ):
    input = config[ 'general' ][ 'Input' ]
else:
    logger.fatalError( 'Must provide file name via command line or settings.' )
    exit()

print( 'Reading data from ' + input + '...\n' )

seedcfg = config[ 'general' ][ 'Seed' ]

if( seedcfg == '' ):
    handler = DigimonWorldHandler( input, logger )
else:
    try:
        handler = DigimonWorldHandler( input, logger, seed=int( seedcfg ) )
    except ValueError:
        logger.fatalError( 'Seed must be an integer. ' + str( seedcfg ) + ' is not a valid value.' )

print( 'Modifying data...\n' )
if( config[ 'starter' ].getboolean( 'Enabled' ) ):
    handler.randomizeStarters( useWeakestTech=config[ 'starter' ].getboolean( 'UseWeakestTech' ) )

if( config[ 'chests' ].getboolean( 'Enabled' ) ):
    handler.randomizeChestItems( allowEvo=config[ 'chests' ].getboolean( 'AllowEvo' ) )

if( config[ 'tokomon' ].getboolean( 'Enabled' ) ):
    handler.randomizeTokomonItems( consumableOnly=config[ 'tokomon' ].getboolean( 'ConsumableOnly' ) )

if( config[ 'mapItems' ].getboolean( 'Enabled' ) ):
    handler.randomizeMapSpawnItems( foodOnly=config[ 'mapItems' ].getboolean( 'FoodOnly' ) )

if( config[ 'evolution' ].getboolean( 'Enabled' ) ):
    handler.randomizeEvolutions()

#If an output file was passed or set, use that as the output.
#Otherwise, read and write the same file
if( len(sys.argv) > 2 ):
    output = sys.argv[2]
elif( config[ 'general' ][ 'Output' ] != '' ):
    output = config[ 'general' ][ 'Output' ]
else:
    output = input

print( 'Writing to ' + output + '...\n' )
handler.write( output )

if( not logger.error ):
    print( 'Modifications complete.  See log file for details (Warning: spoilers!).' )
    print( 'Seed was ' + str( handler.randomseed ) )
    print( 'Enter this seed in settings file to produce the same ROM again.' )
    input( 'Press Enter to finish...' )
else:
    print( 'Program ended with errors.  See log file for details.' )
    input( 'Press Enter to finish...' )
