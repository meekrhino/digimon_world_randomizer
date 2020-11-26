# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

"""
Hard coded data values and binary offsets.
"""

lastPartnerDigimon = 0x41
lastNonfinishTech  = 0x39

#Type enum
types = {
            0x01 : 'DATA',
            0x02 : 'VACCINE',
            0x03 : 'VIRUS'
        }

#Level name enum
levels = {
            0x01 : 'FRESH',
            0x02 : 'IN-TRAINING',
            0x03 : 'ROOKIE',
            0x04 : 'CHAMPION',
            0x05 : 'ULTIMATE'
        }

#Level number enum
levelsByName = {
            'FRESH'         : 0x01,
            'IN-TRAINING'   : 0x02,
            'ROOKIE'        : 0x03,
            'CHAMPION'      : 0x04,
            'ULTIMATE'      : 0x05
        }

#Specialty enum
specs = {
            0x00 : 'FIRE',
            0x01 : 'BATTLE',
            0x02 : 'AIR',
            0x03 : 'EARTH',
            0x04 : 'ICE',
            0x05 : 'MECH',
            0x06 : 'FILTH'
        }

#Tech range enum
ranges = {
            0x01 : 'SHORT',
            0x02 : 'LARGE',
            0x03 : 'WIDE',
            0x04 : 'SELF'
        }

#Effect enum
effects = {
            0x00 : 'NONE',
            0x01 : 'POISON',
            0x02 : 'CONFUSE',
            0x03 : 'STUN',
            0x04 : 'FLAT'
        }

#Tech names (enum)
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

#Starter writing
digimonIDFormat   = '<B'

rookies = ( 0x03, 0x04, 0x11, 0x12, 0x1F, 0x20, 0x2D, 0x2E, 0x39 )

techIDFormat      = '<B'
animIDFormat      = '<B'

#Evolution stat gain patch
evoItemPatchOffset = 0x14CF5AFC
evoItemPatchValue  = 0x00
evoitemPatchFormat = '<B'

#"Woah!" text on item pickup
woahPatchOffset = 0x14D76EF4
woahPatchFormat = '<10s'

#Gabumon enemy stats
gabuPatchFormat = '<h'
gabuPatchWrites = (
            ( 0x0A7EEA8C, 0x7530 ), #CurrentHP 30,000
            ( 0x0A7EEA8E, 0x7530 ), #CurrentMP 30,000
            ( 0x0A7EEA90, 0x7530 ), #MaxHP 30,000
            ( 0x0A7EEA92, 0x7530 ), #MaxMP 30,000
            ( 0x0A7EEA94, 0x7D0  ), #Offense 2,000
            ( 0x0A7EEA96, 0x7D0  ), #Defense 2,000
            ( 0x0A7EEA98, 0x7D0  ), #Speed 2,000
            ( 0x0A7EEA9A, 0x7D0  ), #Brains 2,000
            ( 0x0A7EEA9C, 0x1    ), #Bits 1
            )


#Tier 1 learn chance from brain training
tierOneTechLearnOffset = 0x14C8E58C
tierOneTechLearnValue = 0x28
tierOneTechLearnFormat = '<B'

#Location of script within binary
scriptOffsetInBinary = 0x13FD5809

#Chest items
chestItemFormat   = '<BB'

chestItemOffsets = (
            0x13FE3118, 0x13FE6844, 0x13FEE01E, 0x13FEE02A, 0x13FEE036, 0x13FF4DE8, 0x13FF4DF4, 0x13FF6978,
            0x13FF6984, 0x13FFA098, 0x13FFD7BC, 0x13FFE0F0, 0x13FFF35C, 0x14000EDC, 0x14000EE8, 0x14000EF4,
            0x14003398, 0x140033A4, 0x14005868, 0x140073E8, 0x140073F4, 0x14008F7C, 0x14021168, 0x14021174,
            0x14022D04, 0x14023624, 0x14023630, 0x14023F54, 0x14023F60, 0x14030964, 0x140377A8, 0x13FF58AA,
            0x13FF58B6, 0x14038A04, 0x13FFA508, 0x14039338, 0x140396CA, 0x1403AEC4, 0x1403AED0, 0x1403AEDC,
            0x1403AEE8, 0x14045424, 0x1404A6DC, 0x140539EC, 0x140539F8, 0x1405430C, 0x14054318, 0x14054324,
            0x1405836C, 0x14058C9C, 0x14067B7C, 0x1406970C, 0x14073334, 0x14078F1C, 0x14079848, 0x14079854,
            0x14079860, 0x1407986C, 0x1407A178, 0x1407A184, 0x1407AA94, 0x1407AAA0, 0x1407AAAC, 0x1407AAB8,
            0x1407BD46, 0x1407BD52, 0x1407BD5E, 0x1407F430, 0x1407FD54, 0x14080688, 0x14080FB4, 0x140818F4,
            0x14081900,
            )

#Map item spawns
mapItemFormat = '<BB'

mapItemOffsets = (
            0x13FE2800, 0x1407B400, 0x1400D002, 0x13FED804, 0x13FE6CF4, 0x13FEA008, 0x14031C0A, 0x13FEF40C,
            0x13FEE002, 0x1404140E, 0x13FED694, 0x1402C958, 0x1401C812, 0x14010814, 0x1407B416, 0x13FEE018,
            0x13FFAA04, 0x13FED81A, 0x1403C15A, 0x13FEA01E, 0x14031C20, 0x13FEF422, 0x14041424, 0x1401C828,
            0x1401DD5C, 0x1401082A, 0x1407B42C, 0x1400D02E, 0x14011030, 0x13FEA034, 0x1407C35E, 0x1400C836,
            0x1400E838, 0x13FE3AB4, 0x1404143A, 0x13FEC03C, 0x13FDE40A, 0x13FFD040, 0x13FF7C42, 0x13FEC444,
            0x14011046, 0x13FEA04A, 0x1400C84C, 0x1400E84E, 0x13FEA0B8, 0x13FEC052, 0x13FDD856, 0x13FECD64,
            0x13FEC45A, 0x1401105C, 0x140330BA, 0x1403785E, 0x13FEA060, 0x13FDD862, 0x1400E864, 0x13FEC068,
            0x13FFD06C, 0x13FEC470, 0x14011968, 0x14011072, 0x14037874, 0x1400C6CA, 0x13FEA076, 0x14033078,
            0x1400C6E0, 0x13FEC07E, 0x13FF88C0, 0x1401AC82, 0x13FF7C16, 0x14015088, 0x13FEA08C, 0x1403688E,
            0x1400D018, 0x14036EB4, 0x13FF8894, 0x13FEC16E, 0x14034098, 0x1402C0C4, 0x1401509E, 0x1401AF70,
            0x13FEA0A2, 0x140368A4, 0x1401C0A8, 0x140175E6, 0x13FF88AA, 0x14032572, 0x140340AE, 0x13FFB8B4,
            0x13FE10B8, 0x14035478, 0x140368BA, 0x13FE2CDE, 0x13FE7ACA, 0x1401C0BE, 0x13FEC0C0, 0x140160C2,
            0x140340C4, 0x140114C6, 0x140190C8, 0x1401CA9E, 0x13FFB8CA, 0x13FE10CE, 0x140368D0, 0x14014978,
            0x1401C0D4, 0x140314CE, 0x13FEC0D6, 0x140360D8, 0x13FDD878, 0x140340DA, 0x140114DC, 0x13FDD57A,
            0x140200DE, 0x1403DCD0, 0x13FEA0E4, 0x13FEC0EC, 0x140360EE, 0x1402C0F0, 0x140114F2, 0x140200F4,
            0x13FEA0FA, 0x1401ECB8, 0x1401402A, 0x14041558, 0x13FDF102, 0x14036104, 0x1401F71C, 0x13FEED08,
            0x13FF7C2C, 0x13FE6D0A, 0x13FEA10E, 0x14031510, 0x140160D8, 0x1407BD14, 0x13FEC118, 0x13FFC584,
            0x1402C0DA, 0x13FEED1E, 0x1400D920, 0x13FED830, 0x13FE8922, 0x14041D24, 0x1401476E, 0x13FFCD26,
            0x1402C92C, 0x13FDFA32, 0x13FDF12E, 0x13FEA0CE, 0x1401DD88, 0x13FE3134, 0x13FE6CDE, 0x1400D936,
            0x13FE8938, 0x14035C34, 0x14041D3A, 0x13FFC13C, 0x13FF818A, 0x1407BD40, 0x1407BAE0, 0x1402C942,
            0x1403C144, 0x14032546, 0x1403E148, 0x1400FDE0, 0x13FE314A, 0x1401494C, 0x14041D50, 0x13FEF438,
            0x13FFC152, 0x1401498E, 0x13FF8558, 0x140312E4, 0x13FEC15A, 0x1403255C, 0x1403815E, 0x13FECD90,
            0x14014962, 0x13FDD564, 0x13FFBC62, 0x13FFC168, 0x13FF756C, 0x13FF856E, 0x1401DD72, 0x14038174,
            0x13FE9178, 0x13FECD7A, 0x1401197E, 0x13FDD840, 0x13FF7582, 0x14041584, 0x1400D2B4, 0x13FE7188,
            0x13FDF0EC, 0x13FFB18A, 0x13FE918E, 0x13FDD590, 0x13FF7598, 0x1401B594, 0x140160EE, 0x13FDD596,
            0x13FE1598, 0x13FFC59A, 0x13FDD59C, 0x1404159A, 0x13FE719E, 0x1402D7B2, 0x13FFB1A0, 0x1401BEF0,
            0x14014758, 0x140365A4, 0x140339A8, 0x1402D79C, 0x1401B5AA, 0x13FEECF2, 0x13FDFA48, 0x13FDD5B2,
            0x13FE71B4, 0x13FF81B6, 0x140134F4, 0x140365BA, 0x14035C4A, 0x140339BE, 0x1401E5C0, 0x13FF81A0,
            0x13FDD5C8, 0x13FFBC4C, 0x13FED1CA, 0x13FF81CC, 0x140175D0, 0x13FF8E94, 0x140339D4, 0x1403658E,
            0x140421D8, 0x140175A4, 0x140162FA, 0x13FED1E0, 0x13FDF6DA, 0x13FE25E8, 0x1402B6FC, 0x1401E5EC,
            0x140421EE, 0x13FED1F6, 0x140314FA, 0x14042204, 0x13FFD056, 0x13FF9206, 0x1400FE0C, 0x13FEC102,
            0x1401BEDA, 0x13FFAA1A, 0x13FF921C, 0x1400FE22, 0x13FDF706, 0x13FDD85C, 0x14019DB2, 0x13FEF230,
            0x1407BD08, 0x13FF9232, 0x13FDE7B4, 0x1401350A, 0x1400EBB2, 0x13FE6860, 0x1401B75E, 0x1400E244,
            0x13FEF246, 0x13FE68A2, 0x13FF9248, 0x1401CA88, 0x14031ED8, 0x1400C862, 0x13FE038A, 0x1407BD0E,
            0x1400E25A, 0x1402D25C, 0x140175BA, 0x13FDFA5E, 0x1401DA60, 0x13FE8D10, 0x13FF8E68, 0x1403CA6C,
            0x1400E270, 0x1401CA72, 0x13FDFA74, 0x1401DA76, 0x1401FF14, 0x1403A27E, 0x13FF97C0, 0x1403CA82,
            0x1402CE86, 0x1400D288, 0x1401AC6C, 0x1401DA8C, 0x14012290, 0x13FDF118, 0x1403A294, 0x1402CE9C,
            0x13FE3A9E, 0x1402CE70, 0x13FDDE9E, 0x140122A6, 0x13FED6AA, 0x13FFCEA8, 0x14011B1C, 0x13FF8EAA,
            0x14031EAC, 0x1402D272, 0x14012F8A, 0x13FE7AB4, 0x140312B8, 0x140122BC, 0x13FFCEBE, 0x13FED6C0,
            0x13FE6D20, 0x14031EC2, 0x1401BEC4, 0x13FE6876, 0x1400FDF6, 0x1407BACA, 0x140312CE, 0x13FF72D0,
            0x14025478, 0x1403548E, 0x13FFCED4, 0x1400FAD8, 0x13FEC6DA, 0x14036EE0, 0x140162E4, 0x13FE8D26,
            0x13FF72E6, 0x1401FF2A, 0x1400FAEE, 0x1404156E, 0x13FEC6F0, 0x1402B728, 0x1407BAB4, 0x13FF887E,
            0x14036EF6, 0x140312FA, 0x13FF72FC, 0x13FE732A, 0x14010700, 0x1400FB04, 0x1401E5D6, 0x13FEC706,
            0x13FE6308, 0x13FF852C, 0x13FF9B0C, 0x14016310, 0x140251D8, 0x1402B712, 0x13FE7314, 0x13FEC12E,
            0x14010716, 0x1400FB1A, 0x13FDF71C, 0x13FE631E, 0x13FFA9D8, 0x13FFB320, 0x14032530, 0x1403C322,
            0x14016326, 0x13FE5F28, 0x1400DF2A, 0x1401B774, 0x1401F732, 0x14014040, 0x13FDDE88, 0x14011B32,
            0x1401ECE4, 0x13FFB336, 0x1403C338, 0x13FEED34, 0x14036ECA, 0x13FF8E7E, 0x13FE5F3E, 0x13FE7340,
            0x14036578, 0x1401AF44, 0x13FE0348, 0x13FE108C, 0x1401F706, 0x13FF9B4E, 0x13FF9B38, 0x1407C352,
            0x1400C6B4, 0x1403308E, 0x1400DF56, 0x1407C358, 0x1401AF5A, 0x13FE035E, 0x140314E4, 0x13FDD88E,
            0x13FE5370, 0x13FE0374, 0x13FEC094, 0x1403377C, 0x1401ECCE, 0x1400DF40, 0x14039C8C, 0x14014784,
            0x13FE5386, 0x1401E388, 0x1400CFEC, 0x1407C38A, 0x13FF8542, 0x14035462, 0x1403544C, 0x1401AC98,
            0x14033792, 0x13FF9794, 0x13FFA9EE, 0x13FF97D6, 0x13FEC144, 0x1401479A, 0x1400EB9C, 0x13FEF25C,
            0x1401E39E, 0x14012FA0, 0x140150B4, 0x14035C60, 0x1403D3A6, 0x140337A8, 0x1403E604, 0x1401F748,
            0x13FE688C, 0x13FDD82A, 0x1401E3B4, 0x1400D29E, 0x14012FB6, 0x1403EFB8, 0x14031BF4, 0x1403D3BC,
            0x13FEED4A, 0x13FEDFC0, 0x13FDEBC4, 0x1407BA9E, 0x1401ECFA, 0x1400EBC8, 0x1400D94C, 0x13FDE7CA,
            0x13FE10A2, 0x14011508, 0x13FEDFD6, 0x13FE43D8, 0x140330A4, 0x13FDEBDA, 0x13FE9FDC, 0x13FDF6F0,
            0x1400EBDE, 0x13FDE7E0, 0x13FF7C00, 0x14039CA2, 0x1407B3EA, 0x13FEDFEC, 0x13FE43EE, 0x13FDEBF0,
            0x13FE9FF2, 0x13FDE3F4, 0x1400D272, 0x140413F8, 0x13FFBC78, 0x1401C7FC, 0x13FEC0AA
            )

#Recruitment town triggers
recruitFormat = '<H'

#(if trigger list, trigger, name list, digimon).
recruitOffsets = (
            ( ( 0x14059A40, 0x1405CA20, 0x1405CB42, 0x1405E344, 0x1406AB0A, 0x1405E6C2, 0x14060890, 0x1405C40A,
                0x1405E222, 0x1402C5AE, 0x1405E044, 0x13FE581A, 0x13FD893A, 0x1405CD5C, 0x13FE503A, 0x1405E420,
                0x1406D050, 0x1405C6A2, 0x1402BBE6, 0x1406D7E6, 0x14063CE2, 0x1406BC52, 0x1406F12E, 0x1405E9B0,
                0x13FE5D32, 0x140B4572, 0x13FD8A4A, 0x140B9ABA, 0x1405C14A, 0x140B9BCA ),
              ( 0x13FE9066, 0x13FE9BC8 ),
              204, 0x04 ), #Betamon
            #( ( 0x140B51F6, ), 205 ), #Greymon
            ( ( 0x1406FE82, 0x1406F0A4, 0x140B6668, 0x13FE44A2, 0x140BA898, 0x140701D2, 0x140BA7B4, 0x13FD9718,
                0x13FD9634, 0x13FE543A, 0x1406D75C ),
              (),
              206, 0x06 ), #Devimon
            ( ( 0x13FE5A02, 0x1406D806, 0x14063D02, 0x1406AC0E, 0x140BA318, 0x1406B784, 0x13FE591E, 0x13FD9120,
                0x13FE5222, 0x1402BC06, 0x14059C28, 0x1406AB2A, 0x1406D238, 0x1406BE3A, 0x13FE513E, 0x140BA442,
                0x14059B44, 0x1406C646, 0x1406F14E, 0x13FE5D52, 0x1406D154, 0x1406BD56, 0x1402C5CE, 0x13FE505A,
                0x13FE583A, 0x14059A60, 0x1406C9E6, 0x1405C16A, 0x1406D070, 0x1406BC72, 0x140BA176, 0x14060A78,
                0x140AD37A, 0x1402BCEA, 0x1406C07E, 0x1406D484, 0x1405218A, 0x13FD9198, 0x14060994, 0x1402C796,
                0x1405EB98, 0x140BA2A0, 0x140598A4, 0x1405BFAE, 0x140608B0, 0x1402C6B2, 0x1405EAB4, 0x1405C5B6,
                0x140B47C0, 0x13FD92C2, 0x14051FC6, 0x14063ECA, 0x1402BDCE, 0x1405E9D0, 0x1405C24E, 0x1406B3DE,
                0x140AEBE2, 0x14063DE6, 0x1406D8EA, 0x1406ACF2, 0x13FD8FF6, 0x1406D9CE ),
              ( 0x1401727C, ),
              208, 0x08 ), #Tyrannomon
            ( ( 0x1406D802, 0x13FD9108, 0x1406AC0A, 0x1402BC02, 0x1406C910, 0x1406C516, 0x140AD31A, 0x13FE521E,
                0x14059C24, 0x1406AB26, 0x140BA42A, 0x1405C5B2, 0x1406D234, 0x1406BE36, 0x13FE513A, 0x14059B40,
                0x13FE5836, 0x1406F14A, 0x13FE5D4E, 0x1406D150, 0x1406BD52, 0x1406D354, 0x13FE5056, 0x140BA15A,
                0x14059A5C, 0x1406C362, 0x1402BCE6, 0x1405C166, 0x1406D06C, 0x1406BC6E, 0x14060A74, 0x13FD917C,
                0x140B4880, 0x140AEB82, 0x14052186, 0x140BA288, 0x1406B6C2, 0x14060990, 0x1402C792, 0x1405EB94,
                0x13FE591A, 0x140598A0, 0x13FD92AA, 0x140608AC, 0x1402C6AE, 0x1405EAB0, 0x1406B2B2, 0x1405C24A,
                0x14051FC2, 0x14063EC6, 0x1406D9CA, 0x1405E9CC, 0x1402BDCA, 0x13FD8FDA, 0x1402C5CA, 0x14063DE2,
                0x1406D8E6, 0x1406BF52, 0x1406ACEE, 0x13FE59FE, 0x140BA2FC, 0x1405BFAA, 0x14063CFE ),
              ( 0x13FF55CA, ),
              209, 0x09 ), #Meramon
            ( (),
              (),
              210, 0x0A ), #Seadramon -- does nothing in town and has no Jijimon message
            ( ( 0x1406D760, 0x13FD95E0, 0x1406FC62, 0x13FE44A6, 0x1406FFC8, 0x140B5A62, 0x140BA760, 0x140BA850,
                0x1406F0A8, 0x13FD96D0, 0x13FE543E ),
              ( 0x140745F6, ),
              211, 0x0B ), #Numemon
            ( ( 0x13FD9700, 0x140BA880, 0x1406D764, 0x13FE5446, 0x1406F0AC, 0x1407012E, 0x13FE44AE, 0x140BA798,
                0x140B598E, 0x13FD9618, 0x1406FDDC ),
              ( 0x13FED010, 0x13FED476, 0x13FEDAB0, 0x1404CF06, 0x1404D9D0 ),
              213, 0x0D ), #Mamemon
            #( ( 0x140B644A, ), 214, 0x0E ), #Monzaemon
            ( ( 0x14067588, 0x13FD8F0C, 0x140BA08C, 0x140672CE, 0x140B563C ),
              ( 0x14036030, 0x14036C76, 0x1403729C, 0x14037C1A, 0x1403851A, 0x14038FB0, 0x14039AE2 ),
              217, 0x11 ), #Gabumon
            ( ( 0x13FD89F0, 0x1405C5E2, 0x140B4D44, 0x1405C556, 0x1405C4E6, 0x1405C56A, 0x13FD8C72, 0x140B9B70,
                0x140B9DF2, 0x1405C596, 0x1405C084, 0x1405997A ),
              ( 0x1400DCD6, ),
              218, 0x12 ), #Elecmon
            ( ( 0x1402E900, 0x140B8BF0, 0x14030F06, 0x140319C6, 0x1402E308, 0x1402FECC, 0x1402DBAC, 0x1402E090,
                0x1402DE34, 0x14032398, 0x13FD7A70, 0x140B5B3A, 0x1402E6BE ),
              ( 0x140294CC, ),
              219, 0x13 ), #Kabuterimon
            #( ( 0x140B54BA, ), 220, 0x14 ), #Angemon
            #( ( 0x140B4BCE, ), 221, 0x15 ), #Birdramon
            ( ( 0x1406B880, 0x13FE5A06, 0x1406D80A, 0x13FD9012, 0x140AEC2E, 0x1406CADA, 0x13FE5922, 0x14063D06,
                0x13FE5226, 0x14059C2C, 0x1406AB2E, 0x140BA334, 0x13FD9138, 0x140608B4, 0x1406D23C, 0x1402BC0A,
                0x13FE583E, 0x1406C742, 0x14059B48, 0x1405EAB8, 0x1406F152, 0x13FE5D56, 0x1406D158, 0x1406BD5A,
                0x13FE505E, 0x14059A64, 0x1406AC12, 0x1405C16E, 0x1406D9D2, 0x1406D074, 0x1406BE3E, 0x1406BC76,
                0x140BA45A, 0x1406C17A, 0x14060A7C, 0x1406D580, 0x13FE5142, 0x1405218E, 0x140BA192, 0x1402BCEE,
                0x14060998, 0x1402C79A, 0x1405EB9C, 0x140598A8, 0x1405BFB2, 0x13FD91B4, 0x1402C6B6, 0x140BA2B8,
                0x1405C5BA, 0x140AD3C6, 0x14051FCA, 0x14063ECE, 0x1402C5D2, 0x1405E9D4, 0x13FD92DA, 0x140B4B26,
                0x14063DEA, 0x1406B4DA, 0x1402BDD2, 0x1406D8EE, 0x1405C252, 0x1406ACF6 ),
              ( 0x1401F5FE, ),
              222, 0x16 ), #Garurumon
            ( ( 0x14060A80, 0x1406C280, 0x140BA472, 0x1402BDD6, 0x14063D0A, 0x140B118C, 0x13FE5842, 0x1406D80E,
                0x14052192, 0x13FD902E, 0x1406CC16, 0x1406B99A, 0x1406099C, 0x13FE5D5A, 0x1402C79E, 0x1405EBA0,
                0x13FE5926, 0x140AEEAA, 0x140598AC, 0x1405C172, 0x140BA1AE, 0x14059C30, 0x1406AB32, 0x1405BFB6,
                0x140608B8, 0x1402C6BA, 0x1405EABC, 0x13FE5A0A, 0x1405C5BE, 0x1406D240, 0x1406BE42, 0x1406C844,
                0x13FE5146, 0x1402C5D6, 0x1402BCF2, 0x14059B4C, 0x1405C256, 0x14051FCE, 0x140BA350, 0x14063ED2,
                0x1406AC16, 0x1402BC0E, 0x1406F156, 0x1405E9D8, 0x140B4A80, 0x1406D15C, 0x1406ACFA, 0x1406BD5E,
                0x1406B5E0, 0x13FD9150, 0x13FE5062, 0x1406D9D6, 0x14063DEE, 0x14059A68, 0x1406D8F2, 0x13FD91D0,
                0x1406D078, 0x13FD92F2, 0x1406BC7A, 0x140BA2D0, 0x13FE522A ),
              ( 0x14040D2E, ),
              223, 0x17 ), #Frigimon
            ( ( 0x140B57F4, 0x13FD86FC, 0x1405BF76, 0x140B987C, 0x1405986C, 0x1405B1FE ),
              ( 0x1404507C, ),
              224, 0x18 ), #Whamon
            #( ( 0x140B46F0, ), 225, 0x19 ), #Vegiemon
            ( ( 0x140B68BE, ),
              (),
              226, 0x1A ), #SkullGreymon  -- does nothing except tournament
            ( ( 0x13FD9982, 0x140B617C, 0x140BAB02 ),
              ( 0x1404CEFC, 0x1404D9C6 ),
              227, 0x1B ), #MetalMamemon
            ( ( 0x13FD91F0, 0x140BA370, 0x13FD904E, 0x140AEEEA, 0x140B11CC, 0x140B626E, 0x140BA1CE ),
              ( 0x13FEEC54, 0x1407C2BE, 0x1407CCDC ),
              228, 0x1C ), #Vademon
            ( ( 0x140B9BD6, 0x1406086C, 0x1402C58A, 0x1405E98C, 0x1402BBC2, 0x13FE5D0E, 0x13FE5016, 0x14059A1C,
                0x140BA49E, 0x140BA122, 0x13FD8946, 0x1405C126, 0x1406D02C, 0x1406BC2E, 0x1405C6B0, 0x13FD931E,
                0x1406F10A, 0x14072B0A, 0x14063CBE, 0x13FD9560, 0x1406D7C2, 0x13FE57F6, 0x140B9AC6, 0x1405E6A2,
                0x13FD8A56, 0x140598D8, 0x1406DADE, 0x140BA6E0, 0x1405BFE2, 0x1406AAE6, 0x1405C3EA, 0x1407056C,
                0x14072670, 0x1405C972, 0x1406E176, 0x140B507C, 0x13FD8FA2 ),
              ( 0x1400E69C, ),
              231, 0x1F ), #Patamon
            ( ( 0x1405E4C6, 0x13FE5B08, 0x140B6C4A, 0x13FE438C, 0x1405C50E, 0x13FE5614, 0x13FD8CAE, 0x140B9E2E,
                0x13FE43B0, 0x13FE5324, 0x13FE5B2C, 0x13FD89B2, 0x140B432E, 0x13FE55F0, 0x13FE5348, 0x140B9B32 ),
              ( 0x13FDE31A, ),
              232, 0x20 ), #Kunemon
            ( ( 0x13FD9356, 0x1406E30A, 0x13FD9590, 0x1406F112, 0x1405E994, 0x13FE5D16, 0x13FE501E, 0x14059A24,
                0x1405E6AA, 0x1405C12E, 0x1406D034, 0x140B9BDE, 0x1406BC36, 0x140B4FB8, 0x14060874, 0x1406D7CA,
                0x1406DDC2, 0x14063CC6, 0x1402BBCA, 0x140B9ACE, 0x1405C6B8, 0x13FD894E, 0x140BA4D6, 0x1402C592,
                0x13FD8A5E, 0x140598E0, 0x140BA710, 0x1405BFEA, 0x14072B12, 0x1406AAEE, 0x13FD8FAA, 0x1405C3F2,
                0x14070574, 0x14072678, 0x1405C97A, 0x140BA12A, 0x13FE57FE ),
              ( 0x13FEE4D6, 0x13FEF912, 0x13FF0B34, 0x1407B97C ),
              233, 0x21 ), #Unimon
            ( ( 0x13FD8BD2, 0x140B9D52, 0x140B5E82 ),
              ( 0x13FF193E, ),
              234, 0x22 ), #Ogremon
            ( ( 0x13FD8BF6, 0x1405E4A4, 0x140B9D76, 0x13FD8BBE, 0x1405C4EA, 0x140B9B0A, 0x1405C496, 0x140B4C64,
                0x13FD898A, 0x140B9D3E ),
              ( 0x1403967A, 0x14039A0C ),
              235, 0x23 ), #Shellmon
            #( ( 0x140B43DC, ), 236, 0x24 ), #Centarumon
            ( ( 0x13FD8970, 0x140B9AF0, 0x13FD8C4A, 0x140B9DCA, 0x140B462E ),
              ( 0x13FF7FB2, 0x13FF8C34, 0x13FF95B0, 0x13FF9EBA ),
              237, 0x25 ), #Bakemon
            ( ( 0x140B5568, 0x14059854, 0x1405B1E4, 0x1405BF5E ),
              ( 0x13FF6416, 0x13FF6E38, 0x13FF7912 ),
              238, 0x26 ), #Drimogemon
            ( ( 0x13FD87F6, 0x140B9976 ),
              (),
              239, 0x27 ), #Sukamon -- no Jijimon
            ( ( 0x13FD8780, 0x140B9900, 0x140B6990 ),
              ( 0x1404FAA2, 0x140519FA ),
              240, 0x28 ), #Andromon
            ( ( 0x140B5DE0, 0x1405E514 ),
              ( 0x14052A40, 0x14052D5C ),
              241, 0x29 ), #Giromon
            ( ( 0x13FDD278, 0x13FE0010, 0x13FD63CA, 0x140B754A, 0x140B60CE ),
              ( 0x13FDF51C, 0x13FDFE62 ),
              242, 0x2A ), #Etemon
            ( ( 0x14072B0E, 0x1405E990, 0x13FE5D12, 0x13FE501A, 0x13FD8A5A, 0x14059A20, 0x14060870, 0x1406D7C6,
                0x140BA126, 0x1405C12A, 0x140B5132, 0x1406D030, 0x1406BC32, 0x1405C6B4, 0x13FD933A, 0x140B9ACA,
                0x1406E240, 0x14063CC2, 0x1402BBC6, 0x13FD894A, 0x13FD9578, 0x1406DC52, 0x1406F10E, 0x1402C58E,
                0x140B9BDA, 0x140598DC, 0x140BA4BA, 0x1405E6A6, 0x1405BFE6, 0x1406AAEA, 0x1405C3EE, 0x14070570,
                0x14072674, 0x1405C976, 0x13FD8FA6, 0x140BA6F8, 0x13FE57FA ),
              ( 0x1400F8E0, ),
              245, 0x2D ), #Biyomon
            #( ( 0x140B4266, ), 246, 0x2E ), #Palmon
            ( ( 0x13FE5802, 0x14072B16, 0x13FD8FAE, 0x1406F116, 0x1405E998, 0x13FE5D1A, 0x13FE5022, 0x14059A28,
                0x140BA4F2, 0x1405E6AE, 0x1406DF30, 0x1405C132, 0x1406BC3A, 0x1405C6BC, 0x1406E3BE, 0x1402C596,
                0x14063CCA, 0x140B9BE2, 0x1406D7CE, 0x140B4ED0, 0x14060878, 0x13FD8952, 0x1402BBCE, 0x13FD8A62,
                0x13FD95A8, 0x140598E4, 0x140B9AD2, 0x1405BFEE, 0x140BA728, 0x1406AAF2, 0x140BA12E, 0x1405C3F6,
                0x14070578, 0x1407267C, 0x13FD9372, 0x1405C97E ),
              ( 0x14000BDC, ),
              247, 0x2F ), #Monochromon
            ( ( 0x140B5F30, 0x13FD8ED2, 0x140BA052 ),
              ( 0x140128F0, ),
              248, 0x30 ), #Leomon
            ( ( 0x1405C63A, 0x1405C68A, 0x1406AB0E, 0x1405C612, 0x14060894, 0x13FE581E, 0x1405E424, 0x1405C626,
                0x1405CA28, 0x1405E22A, 0x1402C5B2, 0x1406F132, 0x1405E9B4, 0x13FE5D36, 0x13FD8FBA, 0x1405E03C,
                0x13FE503E, 0x140B44C0, 0x14059A44, 0x1405CB46, 0x1405E348, 0x1405C64E, 0x1406D054, 0x1405C14E,
                0x1406BC56, 0x140B6DDC, 0x140BA13A, 0x1405CD60, 0x1405C662, 0x14063CE6, 0x1406D7EA, 0x1405C676,
                0x1405E47C, 0x1402BBEA, 0x1405C5FE ),
              ( 0x13FE08B0, ),
              249, 0x31 ), #Coelamon
            ( ( 0x140B9946, 0x13FD87C6, 0x14059908, 0x1405994A, 0x1405C012, 0x1405C054, 0x140B4E06, 0x13FD873A,
                0x140B98BA ),
              ( 0x14032E4A, ),
              250, 0x32 ), #Kokatorimon
            ( ( 0x13FD7A82, 0x140B5D3C, 0x140B8C02 ),
              ( 0x1402A706, ),
              251, 0x33 ), #Kuwagamon
            ( ( 0x13FE5442, 0x140B58A4, 0x1406FD28, 0x140BA77C, 0x13FE44AA, 0x13FD96E8, 0x1407006E, 0x1406F0B0,
                0x1406D768, 0x140BA868, 0x13FD95FC ),
              ( 0x1403CE4E, 0x1403D17C, 0x1403D788, 0x1403DAB6, 0x1403E04E ),
              252, 0x34 ), #Mojyamon
            ( ( 0x13FD8F5A, 0x140BA0DA, 0x140B63C6 ),
              (),
              253, 0x35 ), #Nanimon
            ( (),
              (),
              254, 0x36 ), #Megadramon -- does nothing and has no Jijimon message
            ( ( 0x140B600A, 0x13FD9396, 0x140BA516 ),
              ( 0x13FE6B1A, 0x13FE6F98, 0x13FE75D6 ),
              255, 0x37 ), #Piximon
            ( ( 0x13FD9210, 0x140BA390, 0x13FD906E, 0x140AEF36, 0x140B67EE, 0x140BA1EE ),
              ( 0x140774C8, 0x140788B0 ),
              256, 0x38 ), #Digitamamon
            ( ( 0x14066400, 0x140BAB1E, 0x140632A4, 0x140B53E6, 0x140663AC, 0x14063250, 0x14066374, 0x14095A7E,
                0x14063218, 0x1409761C, 0x13FD999E ),
              ( 0x14096804, ),
              257, 0x39 ), #Penguinmon
            ( ( 0x140B573A, 0x13FD95CE, 0x140BA74E ),
              ( 0x13FE4AD6, ),
              258, 0x3A )  #Ninjamon
            )

#Special evolution target
specEvoFormat = '<B'

specEvoOffsets = (
            ( ( 0x140466BF, 0x14046693, 0x14046841, 0x13FD8065, 0x140479ED ),
              0x0E, 0x0B ), #Monzaemon/Toy Town
            ( ( 0x14054503, ),
              0x29, 0x0D ), #Giromon
            ( ( 0x14054589, ),
              0x1B, 0x0D ), #MetalMamemon
            ( ( 0x140A2E11, ),
              0x25, 0x03 ), #Bakemon
            ( ( 0x140A2E5D, ),
              0x1A, 0x0C ), #SkullGreymon
            ( ( 0x140A2EA9, ),
              0x3B, 0x32 ), #Phoenixmon
            ( ( 0x140A2EFB, ),
              0x06, 0x14 ), #Devimon
            ( ( 0x14D19FEC, ),
              0x07, 0x0A ), #Airdramon
            ( ( 0x14D1A01C, ),
              0x3A, 0x19 ), #Ninjamon
            ( ( 0x14D1A054, ),
              0x2F, 0x26 ), #Monochromon
            ( ( 0x14D1A0AC, ),
              0x20, 0x02 ), #Kunemon
            ( ( 0x14D1A0F8, ),
              0x31, 0x18 ), #Coelamon
            ( ( 0x14D1A114, ),
              0x35, 0x35 ), #Nanimon
            ( ( 0x14D1A148, ),
              0x1C, 0x1C ), #Vademon
            ( ( 0x14CD7578, 0x14CD7584 ),
              0x27, 0x27 )  #Sukamon
            )

#Tokomon item gifts
tokoItemFormat = '<BxBB'

tokoItemOffsets = (
            0x14071064,
            0x14071068,
            0x1407106C,
            0x14071070,
            0x14071074,
            0x14071078,
            )

#Tech gift give and check 
learnMoveFormat = '<2B'

learnMoveOffsets = (
            0x14029E3E,     #bug
            0x13FE219A,     #seadra1
            0x13FE21E4,     #seadra2
            0x13FE2232      #seadra3
            )

checkMoveFormat = '<B'

checkMoveOffsets = (
            0x14029B32,     #bug
            0x13FE2192,     #seadra1
            0x13FE21DC,     #seadra2
            0x13FE222A      #seadra3
            )

#Technique data
techDataFormat           = '<3H8Bxx'

techDataBlockOffset      = 0x14D66DF4
techDataBlockSize        = 0x8C0
techDataBlockCount       = 0x79

techDataExclusionOffsets = (
            0x14D673B8,
            )
techDataExclusionSize    = 0x130

#Technique battle learn chance block
techLearnFormat          = '<BBB'

techLearnBlockOffset     = 0x14D66A2C
techLearnBlockSize       = 0x1DE
techLearnBlockCount      = 0x3A

techLearnExclusionOffsets= (
            0x14D66A88,
            )
techLearnExclusionSize   = 0x130

#Technique brain learn chance block
techBrainFormat          = '<BBB'

techBrainBlockOffset     = 0x14C8E58C
techBrainBlockSize       = 0x18
techBrainBlockCount      = 0x08

techBrainExclusionOffsets= (
            )
techBrainExclusionSize   = 0x130

#Technique tier list table
techTierListFormat       = '<8B'

techTierListBlockOffset  = 0x14C8E554
techTierListBlockSize    = 0x38
techTierListBlockCount   = 0x07

techTierListExclusionOffsets = (    #no exclusions in this block since it is tiny
            )
techTierListExclusionSize= 0x130

#Digimon data
digimonDataFormat        = '<20sihh23Bx'

digimonDataBlockOffset   = 0x14D6E9DC       #start of digimon data block
digimonDataBlockSize     = 0x2A80           #total number of bytes
digimonDataBlockCount    = 0xB4             #number of digimon blocks

digimonDataExclusionOffsets = (
            0x14D6EB28, #in Devimon
            0x14D6F458, #in Biyomon
            0x14D6FD88, #in Piddomon
            0x14D706B8, #in Master Tyrannomon
            0x14D70FE8  #in Biyomon
            )
digimonDataExclusionSize = 0x130

#Digivolution to/from table
evoToFromFormat          = '<11B'

evoToFromBlockOffset     = 0x14D6CE04       #start of evo to/from block
evoToFromBlockSize       = 0x3DA            #total number of bytes
evoToFromBlockCount      = 0x3E

evoToFromExclusionOffsets= (
            0x14D6CF98, #in to Bakemon 3-4
            )
evoToFromExclusionSize   = 0x130

#Digivolution stat gains
evoStatsFormat           = '<6HH'

evoStatsBlockOffset      = 0x14D6CA68       #start of evo stats block
evoStatsBlockSize        = 0x39C            #total number of bytes
evoStatsBlockCount       = 0x42

evoStatsExclusionOffsets = (
            )
evoStatsExclusionSize    = 0x130

#Digivolution requirements
evoReqsFormat            = '<11Hh2H'

evoReqsBlockOffset       = 0x14D6C254       #start of evo to/from block
evoReqsBlockSize         = 0x814            #total number of bytes
evoReqsBlockCount        = 0x3F

evoReqsExclusionOffsets  = (
            0x14D6C668, #in Bakemon
            )
evoReqsExclusionSize     = 0x130

#Item data
itemDataFormat           = '<20sIHHb?2x'

itemDataBlockOffset      = 0x14D676C4       #start of item data block
itemDataBlockSize        = 0x1260           #total number of bytes
itemDataBlockCount       = 0x80             #number of item blocks

itemDataExclusionOffsets = (
            0x14D67CE8, #in Red Berry
            0x14D68618, #in Coral charm
            )
itemDataExclusionSize    = 0x130

#Giromon jukebox track name list
trackNameBlockOffset     = 0x14D717E8       #start of item data block
trackNameBlockSize       = 0x738            #total number of bytes

trackNameExclusionOffsets= (
            0x14D71918, #in Lava Cave Theme
            )
trackNameExclusionSize   = 0x130

#Injecting hash into Jijimon
introHashOffset          = 0x140BD212

#Intro scene skip
introSkipOutsideDest     = 2306
introSkipOutsideOffset   = 0x1407DA20 # just after "Welcome to Digimon World"

introSkipInsideDest      = 5108
introSkipInsideOffset    = 0x1407E44C # just after "I invited you here\nto save us"

#Unrigged slots
unrigSlotsFormat         = '<I'
unrigSlotsValue          = 0x08023A1E #should be written to little endian, this is 'reverse' order
unrigSlotsOffset         = 0x14C8DB10 # TRN_REL.BIN

unrigSlots2Format         = '<I'
unrigSlots2Value          = 0x08023494
unrigSlots2Offset         = 0x14C941F8 # TRN_REL2.BIN

#Update PP calculation function
rewritePPFormat          = '>IIIIIIIIIII' #write as big endian, because these instructions are 'forwards' order
rewritePPValue           = ( 0x0F19040C, 0xFFFF6432, 0x1E004010, 0x00000000, 0x1380023C, 0xCECE4224, 0x21105200, 0x00004290, 
                             0x03004230, 0x21885100, 0x16000010 )
rewritePPOffset          = 0x14D2848C

#Fix rotation softlock
fixRotationSLFormat      = "B"
fixRotationSLValue       = 0x0D
fixRotationSLOffset      = ( 0x14CE72C0, 0x14CE7464 )

#Fix entityMoveTo softlock
fixMoveToSLFormat        = "<I"
fixMoveToSLValue         = 0x10400006
fixMoveToSLOffset        = ( 0x14CDB140, 0x14CDB19C )

#Fix Toy Town softlock
fixToyTownSLFormat       = ">I"
fixToyTownSLValue        = 0x31FCA302
fixToyTownSLOffset       = ( 0x14049DD8, 0x1404A2EA )

#Fix Leomon's Cave Nanimon softlock
fixLeoCaveSLFormat       = "B"
fixLeoCaveSLValue        = 0x3B
fixLeoCaveSLOffset       = ( 0x14030380, 0x14030444, 0x14030D36, 0x14030DFA, 0x140317F6, 0x140318BA, 0x140321C8, 0x1403228C )

#Unify evolution target function to free memory
evoTargetUnifyHackFormat = '<I'
evoTargetUnifyHack       = { 0x14CD7520: 0x0C038AED, 0x14D19A14: 0x24050003,
                             0x14D19A20: 0x8FB00018, 0x14D19A2C: 0x16050004, }

#Reset button combination/custom tick function
customTickFunctionFormat = '<9I'
customTickFunctionValue  = ( 0x8F8293B8, 0x200301F0, 0x00430824, 0x14230003,
                             0x240A00A0, 0x01400008, 0x240900A0, 0x03E00008,
                             0x00000000, )
customTickFunctionOffset = 0x14D19A70

customTickHookFormat     = '<I'
customTickHookValue      = 0x24E72F08
customTickHookOffset     = 0x14D1A388

#Unlock type-locked areas
unlockTypeLockFormat     = '<H'

unlockGreylordValue      = 1226
unlockGreylordOffset     = ( 0x13FF808E, )

unlockIceValue           = 60
unlockIceOffset          = ( 0x1401D130, 0x1401D2A8 )

unlockToyTownFormat      = '<I'
unlockToyTownValue       = 0x015D0001
unlockToyTownOffset      = ( 0x140479EA, )

#Ogremon 2 / Nanimon softlock
ogremonSoftlockFormat    = '<H'
ogremonSoftlockValue     = 235
ogremonSoftlockOffset    = ( 0x13FD689A, 0x140B7A1A )

#Spawn rate for RNG digimon recruit spawns
spawnRateFormat          = '<B'
spawnRateMamemonOffset   = ( 0x13FD678F, 0x140B790F )
spawnRatePiximonOffset   = ( 0x13FD64DB, 0x13FDD389, 0x13FE0121, 0x140B765B )
spawnRateMMamemonOffset  = ( 0x13FD831F, 0x140B949F )
spawnRateOtamamonOffset  = ( 0x13FD7F47, 0x140B90C7 )

#Starter and starter tech
starterSetDigimonOffset  = ( 0x14D271C0, 0x14D271B8 )   #set digimon id
starterChkDigimonOffset  = ( 0x14CD1D24, 0x14CD1D44 )   #check digimon id to set tech
starterLearnTechOffset   = ( 0x14CD1D40, 0x14CD1D60 )   #tech to learn
starterEquipAnimOffset   = ( 0x14CD1D30, 0x14CD1D50 )   #animation to equip
starterStatChkDigimonOffset = 0x1407E2C5

#type effectiveness 
typeEffectivenessFormat = 'B'
typeEffectivenessOffset = 0x14D669F8
 
#learn move and command patch
learnMoveAndCommandFormat = "<II"
learnMoveAndCommandValue  = ( 0x10000065, 0x00001021 )
learnMoveAndCommandOffset = 0x14C8821C

#DV Chip text patch

DVChipAValue = "Boosts Off+Brains by 100"
DVChipAOffset = 0x14D65F10
DVChipAFormat = "<28s"

DVChipDValue = "Boosts Def+Speed by 100"
DVChipDOffset = 0x14D65F2C
DVChipDFormat = "<28s"

DVChipEValue = "Boosts HP+MP by 1000"
DVChipEOffset = 0x14D65F48
DVChipEFormat = "<28s"

# Change Dragon Eye Lake Vending Machine to HappyShroom
happyMushroomVendingOffset1 = 0x13FE31C8
happyMushroomVendingFormat1 = "<124s"
happyMushroomVendingValue1 = "HappyMushroom: 2000 bits\r\0DigiMushroom: 600 bits\r\0Don「t buy\r\0"

happyMushroomVendingOffset2 = 0x13FE3300
happyMushroomVendingFormat2 = "<36s"
happyMushroomVendingValue2 = "\1\6HappyMushroom \1\1came out!\0\r\0\r\0\r"

happyMushroomVendingOffset3 = 0x13FE3252
happyMushroomVendingOffset4 = 0x13FE32F8
happyMushroomVendingPriceFormat = "<H"
happyMushroomVendingPriceValue = 2000

happyMushroomVendingOffset5 = ( 0x13FE3326, 0x13FE3338, 0x13FE3382 )
happyMushroomVendingFormat5 = "B"
happyMushroomVendingValue5 = 69