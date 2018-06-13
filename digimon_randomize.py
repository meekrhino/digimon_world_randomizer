import random
import sys

rookies = [0x03, 0x04, 0x11, 0x12, 0x1F, 0x20, 0x2D, 0x2E, 0x39]

techs = {
			0x03 : 0x02,
			0x04 : 0X0C,
			0x11 : 0x2B,
			0x12 : 0X0C,
			0x1F : 0x2B,
			0x20 : 0x25,
			0x2D : 0x02,
			0x2E : 0X25,
			0x39 : 0x25
			}
			
equip = {
			0x03 : 0x2E,
			0x04 : 0x2E,
			0x11 : 0x30,
			0x12 : 0X31,
			0x1F : 0x2E,
			0x20 : 0x31,
			0x2D : 0x2E,
			0x2E : 0X2E,
			0x39 : 0x2E
			}

firstDigiOffsets = [0x14CD1D24, 0x14D271B8]
secondDigiOffsets = [0x14D271C0, 0x14CD1D44]
firstTechOffsets = [0x14CD1D40]
secondTechOffsets = [0x14CD1D60]
firstEquipOffsets = [0x14CD1D30]
secondEquipOffsets = [0x14CD1D50]

if( len(sys.argv) < 1 ):
	print( 'Must provide file name at command line.' )
	exit

firstDigi = rookies[random.randint(0, len(rookies) - 1)]
secondDigi = firstDigi
while secondDigi == firstDigi:
	secondDigi = rookies[random.randint(0, len(rookies) - 1)]
	
filename = sys.argv[1]

print( 'Modifying ' + filename )
with open( filename, 'r+' + 'b' ) as file:
	for ofst in firstDigiOffsets:
		file.seek( ofst, 0 )
		value = firstDigi
		print('0x' + format(value, '02x'))
		bytesToWrite = bytes([value])
		str( file.write( bytesToWrite ) )
		
	for ofst in firstTechOffsets:
		file.seek( ofst, 0 )
		value = techs.get( firstDigi )
		print('0x' + format(value, '02x'))
		bytesToWrite = bytes([value])
		str( file.write( bytesToWrite ) )
		
	for ofst in firstEquipOffsets:
		file.seek( ofst, 0 )
		value = equip.get( firstDigi )
		print('0x' + format(value, '02x'))
		bytesToWrite = bytes([value])
		str( file.write( bytesToWrite ) )
	
	for ofst in secondDigiOffsets:
		file.seek( ofst, 0 )
		value = secondDigi
		print('0x' + format(value, '02x'))
		bytesToWrite = bytes([value])
		( file.write( bytesToWrite ) )
	
	for ofst in secondTechOffsets:
		file.seek( ofst, 0 )
		value = techs.get( secondDigi )
		print('0x' + format(value, '02x'))
		bytesToWrite = bytes([value])
		str( file.write( bytesToWrite ) )
		
	for ofst in secondEquipOffsets:
		file.seek( ofst, 0 )
		value = equip.get( secondDigi )
		print('0x' + format(value, '02x'))
		bytesToWrite = bytes([value])
		str( file.write( bytesToWrite ) )

print( 'Modified starting digimon options.' )
