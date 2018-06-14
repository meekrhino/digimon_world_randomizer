import random
import sys
from digimon.handler import DigimonWorldHandler

if( len(sys.argv) < 1 ):
	print( 'Must provide file name at command line.' )
	exit

print( 'Modifying ' + filename = '...' )
handler = DigimonWorldHandler(sys.argv[1])

handler.randomizeStarters()
handler.updateTechs()

handler.write()
print( 'Modified starting digimon options.' )
