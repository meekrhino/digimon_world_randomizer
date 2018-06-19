import random
import sys
from digimon.handler import DigimonWorldHandler

if( len(sys.argv) < 1 ):
	print( 'Must provide file name at command line.' )
	exit

print( 'Reading data from ' + sys.argv[1] + '...' )
handler = DigimonWorldHandler(sys.argv[1])

handler.randomizeStarters()
handler.setStarterTechs( default=True )

if( len(sys.argv) > 1 ):
    out = sys.argv[2]
else:
    out = sys.argv[1]

print( 'Writing to ' + out + '...' )
handler.write( out, verbose=True )

print( 'Modifications complete.' )
