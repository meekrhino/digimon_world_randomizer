import random
import sys
from digimon.handler import DigimonWorldHandler

if( len(sys.argv) < 1 ):
	print( 'Must provide file name at command line.' )
	exit

print( 'Reading data from ' + sys.argv[1] + '...\n' )
handler = DigimonWorldHandler(sys.argv[1])

print( 'Modifying data...\n' )
handler.randomizeStarters()
handler.randomizeChestItems()

if( len(sys.argv) > 1 ):
    out = sys.argv[2]
else:
    out = sys.argv[1]

print( 'Writing to ' + out + '...\n' )
handler.write( out, verbose=False )

print( 'Modifications complete.' )
