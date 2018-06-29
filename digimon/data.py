# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Hard coded data values and binary offsets.
"""

from future.utils import iteritems

names = {
            0x03 : 'Agumon',
            0x04 : 'Betamon',
            0x11 : 'Gabumon',
            0x12 : 'Elecmon',
            0x1F : 'Patamon',
            0x20 : 'Kunemon',
            0x2D : 'Biyomon',
            0x2E : 'Palmon',
            0x39 : 'Penguinmon'
            }

techs = {
            0x00 : 'Fire Tower',
            0x01 : 'Prominence Beam',
            0x02 : 'Spit Fire',
            0x03 : 'Red Inferno',
            0x04 : 'Magma Bomb',
            0x05 : 'Heat Laser',
            0x06 : 'Inifinity Burn',
            0x07 : 'Meltdown',
            0x08 : 'Thunder Justice',
            0x09 : 'Spinning Shot',
            0x0A : 'Electric Cloud',
            0x0B : 'Megalo Spark',
            0x0C : 'Static Elect',
            0x0D : 'Wind Cutter',
            0x0E : 'Confused Storm',
            0x0F : 'Hurricane',
            0x10 : 'Giga Freeze',
            0x11 : 'Ice Statue',
            0x12 : 'Winter Blast',
            0x13 : 'Ice Needle',
            0x14 : 'Water Blit',
            0x15 : 'Aqua Magic',
            0x16 : 'Aurora Freeze',
            0x17 : 'Tear Drop',
            0x18 : 'Power Crane',
            0x19 : 'All Range Beam',
            0x1A : 'Metal Sprinter',
            0x1B : 'Pulse Laser',
            0x1C : 'Delete Program',
            0x1D : 'DG Dimension',
            0x1E : 'Full Potential',
            0x1F : 'Reverse Prog',
            0x20 : 'Poison Powder',
            0x21 : 'Bug',
            0x22 : 'Mass Morph',
            0x23 : 'Insect Plague',
            0x24 : 'Charm Perfume',
            0x25 : 'Poison Claw',
            0x26 : 'Danger Sting',
            0x27 : 'Green Trap',
            0x28 : 'Tremar',
            0x29 : 'Muscle Charge',
            0x2A : 'War Cry',
            0x2B : 'Sonic Jab',
            0x2C : 'Dynamite Kick',
            0x2D : 'Counter',
            0x2E : 'Megaton Punch',
            0x2F : 'Buster Dive',
            0x30 : 'Dynamite Kick v2',
            0x31 : 'Odor Spray',
            0x32 : 'Poop Spd Toss',
            0x33 : 'Big Poop Toss',
            0x34 : 'Big Rnd Toss',
            0x35 : 'Poop Rnd Toss',
            0x36 : 'Rnd Spd Toss',
            0x37 : 'Horizontal Kick',
            0x38 : 'Ult Poop Hell',
            0x39 : 'Horizontal Kick v2',
            0x3A : 'Blaze Blast',
            0x3B : 'Pepper Breath',
            0x3C : 'Lovely Attack',
            0x3D : 'Fireball',
            0x3E : 'Death Claw',
            0x3F : 'Mega Flame',
            0x40 : 'Howling Blaster',
            0x41 : 'Party time',
            0x42 : 'Electric Shock',
            0x43 : 'Abduction Beam',
            0x44 : 'Smiley Bomb',
            0x45 : 'Spnning Needle',
            0x46 : 'Spiral Twister',
            0x47 : 'Boom Bubble',
            0x48 : 'Sweet Breath',
            0x49 : 'Bit Bomb',
            0x4A : 'Deadly Bomb',
            0x4B : 'Drill Spin',
            0x4C : 'Electric Thread',
            0x4D : 'Energy Bomb',
            0x4E : 'Genoside Attack',
            0x4F : 'Giga Scissor Claw',
            0x50 : 'Dark Shot',
            0x51 : 'Pummel Whack',
            0x52 : 'Hand of Fate',
            0x53 : 'Dark Claw',
            0x54 : 'Aerial Attack',
            0x55 : 'Bone Boomerang',
            0x56 : 'Solar Ray',
            0x57 : 'Hydro Pressure',
            0x58 : 'Ice Blast',
            0x59 : 'Iga School Knife Throw',
            0x5A : 'Blasting Spout',
            0x5B : 'Fist of the Beast King',
            0x5C : 'Dark Network & Concert Crush',
            0x5D : 'Electro Shocker',
            0x5E : 'Meteor Wing',
            0x5F : 'Super Slap',
            0x60 : 'Nightmare Syndromer',
            0x61 : 'Frozen Fire Shot',
            0x62 : 'Poison Ivy',
            0x63 : 'Blue Blaster',
            0x64 : 'Scissor Claw',
            0x65 : 'Super Thunder Strike',
            0x66 : 'Spiral Sword',
            0x67 : 'Variable Darts',
            0x68 : 'Volcanic Strike',
            0x69 : 'Subzero Ice Punch',
            0x6A : 'Infinity Cannon',
            0x6B : 'Party time',
            0x6C : 'Party time',
            0x6D : 'Crimson Flare',
            0x6E : 'Glacial Blast',
            0x6F : 'Mail Strome',
            0x70 : 'High Electro Shocker',
            0x71 : 'Bubble',
            0x72 : 'Bubble',
            0x73 : 'Bubble',
            0x74 : 'Bubble',
            0x75 : 'Bubble',
            0x76 : 'Bubble',
            0x77 : 'Bubble',
            0x78 : 'Bubble'
            }

items = {
            0x00 : 'sm.recovery',
            0x01 :'med.recovery',
            0x02 :'lrg.recovery',
            0x03 :'sup.recovery',
            0x04 :'MP Floppy',
            0x05 :'Medium MP',
            0x06 :'Large MP',
            0x07 :'Double flop',
            0x08 :'Various',
            0x09 :'Omnipotent',
            0x0A :'Protection',
            0x0B :'Restore',
            0x0C :'Sup.restore',
            0x0D :'Bandage',
            0x0E :'Medicine',
            0x0F :'Off. Disk',
            0x10 :'Def. Disk',
            0x11 :'Hispeed dsk',
            0x12 :'Omni Disk',
            0x13 :'S.Off.disk',
            0x14 :'S.Def.disk',
            0x15 :'S.speed.disk',
            0x16 :'Auto Pilot',
            0x17 :'Off. Chip',
            0x18 :'Def. Chip',
            0x19 :'Brain Chip',
            0x1A :'Quick Chip',
            0x1B :'HP Chip',
            0x1C :'MP Chip',
            0x1D :'DV Chip A',
            0x1E :'DV Chip D',
            0x1F :'DV Chip E',
            0x20 :'Port. potty',
            0x21 :'Trn. manual',
            0x22 :'Rest pillow',
            0x23 :'Enemy repel',
            0x24 :'Enemy bell',
            0x25 :'Health shoe',
            0x26 :'Meat',
            0x27 :'Giant Meat',
            0x28 :'Sirloin',
            0x29 :'Supercarrot',
            0x2A :'Hawk radish',
            0x2B :'Spiny green',
            0x2C :'Digimushrm',
            0x2D :'Ice mushrm',
            0x2E :'Deluxmushrm',
            0x2F :'Digipine',
            0x30 :'Blue apple',
            0x31 :'Red Berry',
            0x32 :'Gold Acorn',
            0x33 :'Big Berry',
            0x34 :'Sweet Nut',
            0x35 :'Super veggy',
            0x36 :'Pricklypear',
            0x37 :'Orange bana',
            0x38 :'Power fruit',
            0x39 :'Power Ice',
            0x3A :'Speed Leaf',
            0x3B :'Sage Fruit',
            0x3C :'Muscle Yam',
            0x3D :'Calm berry',
            0x3E :'Digianchovy',
            0x3F :'Digisnapper',
            0x40 :'DigiTrout',
            0x41 :'Black trout',
            0x42 :'Digicatfish',
            0x43 :'Digiseabass',
            0x44 :'Moldy Meat',
            0x45 :'Happymushrm',
            0x46 :'Chain melon',
            0x47 :'Grey Claws',
            0x48 :'Fireball',
            0x49 :'Flamingwing',
            0x4A :'Iron Hoof',
            0x4B :'Mono Stone',
            0x4C :'Steel drill',
            0x4D :'White Fang',
            0x4E :'Black Wing',
            0x4F :'Spike Club',
            0x50 :'Flamingmane',
            0x51 :'White Wing',
            0x52 :'Torn tatter',
            0x53 :'Electo ring',
            0x54 :'Rainbowhorn',
            0x55 :'Rooster',
            0x56 :'Unihorn',
            0x57 :'Horn helmet',
            0x58 :'Scissor jaw',
            0x59 :'Fertilizer',
            0x5A :'Koga laws',
            0x5B :'Waterbottle',
            0x5C :'North Star',
            0x5D :'Red Shell',
            0x5E :'Hard Scale',
            0x5F :'Bluecrystal',
            0x60 :'Ice crystal',
            0x61 :'Hair grower',
            0x62 :'Sunglasses',
            0x63 :'Metal part',
            0x64 :'Fatal Bone',
            0x65 :'Cyber part',
            0x66 :'Mega Hand',
            0x67 :'Silver ball',
            0x68 :'Metal armor',
            0x69 :'Chainsaw',
            0x6A :'Small spear',
            0x6B :'X Bandage',
            0x6C :'Ray Gun',
            0x6D :'Gold banana',
            0x6E :'Mysty Egg',
            0x6F :'Red Ruby',
            0x70 :'Beetlepearl',
            0x71 :'Coral charm',
            0x72 :'Moon mirror',
            0x73 :'Blue Flute',
            0x74 :'old fishrod',
            0x75 :'Amazing rod',
            0x76 :'Leomonstone',
            0x77 :'Mansion key',
            0x78 :'Gear',
            0x79 :'Rain Plant',
            0x7A :'Steak',
            0x7B :'Frig Key',
            0x7C :'AS Decoder',
            0x7D :'Giga Hand',
            0x7E :'Noble Mane',
            0x7F :'Metalbanana',
            }

types = {
            0x01 : 'DATA',
            0x02 : 'VACCINE',
            0x03 : 'VIRUS'
        }

levels = {
            0x01 : 'FRESH',
            0x02 : 'IN-TRAINING',
            0x03 : 'ROOKIE',
            0x04 : 'CHAMPION',
            0x05 : 'ULTIMATE'
        }

specs = {
            0x00 : 'FIRE',
            0x01 : 'BATTLE',
            0x02 : 'AIR',
            0x03 : 'EARTH',
            0x04 : 'ICE',
            0x05 : 'MECH',
            0x06 : 'FILTH'
        }

#Everything from 'Grey Claws' to 'Coral charm' and 'Giga Hand' to the end
evoItems = { k:v for k,v in iteritems( items ) if( ( k >= 0x47
                                                 and k <= 0x72 )
                                                  or k >= 0x7D ) }

#Everything from 'Blue Flute' to 'AS Decoder' excluding 'Rain Plant' and 'Steak'
questItems = { k:v for k,v in iteritems( items ) if( k >= 0x73
                                                 and k <= 0x7C
                                                 and v != 'Rain Plant'
                                                 and v != 'Steak' ) }

rookies = ( 0x03, 0x04, 0x11, 0x12, 0x1F, 0x20, 0x2D, 0x2E, 0x39 )

starterTechs = {
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

starterTechSlots = {
            0x03 : 0x01,
            0x04 : 0x01,
            0x11 : 0x03,
            0x12 : 0X04,
            0x1F : 0x01,
            0x20 : 0x04,
            0x2D : 0x01,
            0x2E : 0X01,
            0x39 : 0x01
            }

chestItemOffsets = (
            0x13FE3118, #706
            0x13FE6844,
            0x13FEE01E,
            0x13FEE02A,
            0x13FEE036,
            0x13FF4DE8,
            0x13FF4DF4,
            0x13FF6978,
            0x13FF6984,
            0x13FFA098,
            0x13FFD7BC,
            0x13FFE0F0,
            0x13FFF35C,
            0x14000EDC,
            0x14000EE8,
            0x14000EF4,
            0x14003398,
            0x140033A4,
            0x14005868,
            0x140073E8,
            0x140073F4,
            0x14008F7C,
            0x14021168,
            0x14021174,
            0x14022D04,
            0x14023624,
            0x14023630,
            0x14023F54,
            0x14023F60,
            0x14030964,
            0x140377A8,
            0x13FF58AA,
            0x13FF58B6,
            0x14038A04,
            0x13FFA508,
            0x14039338,
            0x140396CA,
            0x1403AEC4,
            0x1403AED0,
            0x1403AEDC,
            0x1403AEE8,
            0x14045424,
            0x1404A6DC,
            0x140539EC,
            0x140539F8,
            0x1405430C,
            0x14054318,
            0x14054324,
            0x1405836C,
            0x14058C9C,
            0x14067B7C,
            0x1406970C,
            0x14073334,
            0x14078F1C, #707
            0x14079848, #709
            0x14079854, #708
            0x14079860, #710
            0x1407986C, #711
            0x1407A178, #712
            0x1407A184, #713
            0x1407AA94, #700
            0x1407AAA0, #701
            0x1407AAAC, #702
            0x1407AAB8, #703
            0x1407BD46, #696
            0x1407BD52, #697
            0x1407BD5E, #698
            0x1407F430, #686
            0x1407FD54, #687
            0x14080688, #688
            0x14080FB4, #689
            0x140818F4, #690
            0x14081900, #691
            )

digimonDataBlockOffset   = 0x14D6E9DC       #start of digimon data block
digimonDataBlockSize     = 0x2A80           #total number of bytes
digimonDataBlockCount    = 0xB4             #number of digimon blocks

digimonDataExclusionOffsets = (
            0x14D6EB28, #in Devimo
            0x14D6F458, #in Biyomon
            0x14D6FD88, #in Piddomon
            0x14D706B8, #in Master Tyrannomon
            0x14D70FE8  #in Biyomon
            )
digimonDataExclusionSize = 0x130

starter1SetDigimonOffset = 0x14D271C0       #set digimon id for agumon
starter1ChkDigimonOffset = 0x14CD1D24       #check digimon id to set agumon's tech
starter1LearnTechOffset  = 0x14CD1D40       #tech to learn for agumon
starter1EquipAnimOffset  = 0x14CD1D30       #animation to equip for agumon

starter2SetDigimonOffset = 0x14D271B8       #set digimon id for gabumon
starter2ChkDigimonOffset = 0x14CD1D44       #check digimon id to set gabumon's tech
starter2LearnTechOffset  = 0x14CD1D60       #tech to learn for gabuumon
starter2EquipAnimOffset  = 0x14CD1D50       #animation to equip for gabumon
