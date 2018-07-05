# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

import random
import configparser
import sys
from log.logger import Logger
from digimon.handler import DigimonWorldHandler

if( len(sys.argv) < 1 ):
	print( 'Must provide file name at command line.' )
	exit

config = configparser.ConfigParser()
config.read( 'settings.ini' )

verbose = config[ 'general' ].getboolean( 'verbose' )
logger = Logger( verbose, filename='randomize.log' )

logger.logAlways( 'Reading data from ' + sys.argv[1] + '...\n' )

seedcfg = config[ 'general' ][ 'seed' ]

if( seedcfg == 'None' ):
    handler = DigimonWorldHandler( sys.argv[1], logger )
else:
    try:
        handler = DigimonWorldHandler( sys.argv[1], logger, seed=int( seedcfg ) )
    except ValueError:
        print( 'Seed must be an integer. ' + str( seedcfg ) + ' is not a valid value.' )
        exit()

logger.logAlways( 'Modifying data...\n' )
if( config[ 'starter' ].getboolean( 'Enabled' ) ):
    handler.randomizeStarters( useWeakestTech=config[ 'starter' ].getboolean( 'UseWeakestTech' ) )

if( config[ 'chests' ].getboolean( 'Enabled' ) ):
    handler.randomizeChestItems( allowEvo=config[ 'chests' ].getboolean( 'AllowEvo' ) )

if( config[ 'tokomon' ].getboolean( 'Enabled' ) ):
    handler.randomizeTokomonItems( consumableOnly=config[ 'tokomon' ].getboolean( 'ConsumableOnly' ) )

if( config[ 'mapItems' ].getboolean( 'Enabled' ) ):
    handler.randomizeMapSpawnItems( foodOnly=config[ 'mapItems' ].getboolean( 'FoodOnly' ) )

#If a second file was passed, use that as the output.
#Otherwise, read and write the same file
if( len(sys.argv) > 1 ):
    out = sys.argv[2]
else:
    out = sys.argv[1]

logger.logAlways( 'Writing to ' + out + '...\n' )
handler.write( out )

logger.logAlways( 'Modifications complete.' )

if( not logger.error ):
    print( 'Program executed succesfully.  See log file for details (Warning: spoilers!).' )
    print( 'Seed was ' + str( handler.randomseed ) )
    print( 'Enter this seed in settings file to produce the same ROM again.' )
else:
    print( 'Program ended with errors.  See log file for errors.' )
