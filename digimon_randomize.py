# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

import random
import configparser
import sys
from digimon.handler import DigimonWorldHandler

if( len(sys.argv) < 1 ):
	print( 'Must provide file name at command line.' )
	exit

config = configparser.ConfigParser()
config.read( 'settings.ini' )

print( 'Reading data from ' + sys.argv[1] + '...\n' )

verbose = config[ 'general' ].getboolean( 'verbose' )

handler = DigimonWorldHandler( sys.argv[1], verbose )

print( 'Modifying data...\n' )
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

print( 'Writing to ' + out + '...\n' )
handler.write( out )

print( 'Modifications complete.' )
