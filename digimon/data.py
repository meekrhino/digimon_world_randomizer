# Author: Tristan Challener <challenert@gmail.com>
# Copyright: please don't steal this that is all

"""
Hard coded data values and binary offsets.
"""

lastPartnerDigimon = 0x41
lastNonfinishTech  = 0x39

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

levelsByName = {
            'FRESH'         : 0x01,
            'IN-TRAINING'   : 0x02,
            'ROOKIE'        : 0x03,
            'CHAMPION'      : 0x04,
            'ULTIMATE'      : 0x05
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

ranges = {
            0x01 : 'SHORT',
            0x02 : 'LARGE',
            0x03 : 'WIDE',
            0x04 : 'SELF'
        }

effects = {
            0x00 : 'NONE',
            0x01 : 'POISON',
            0x02 : 'CONFUSE',
            0x03 : 'STUN',
            0x04 : 'FLAT'
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

digimonIDFormat   = '<B'

rookies = ( 0x03, 0x04, 0x11, 0x12, 0x1F, 0x20, 0x2D, 0x2E, 0x39 )

techIDFormat      = '<B'
animIDFormat      = '<B'

evoItemPatchOffset = 0x14CF5AFC
evoItemPatchValue  = 0x00
evoitemPatchFormat = '<B'

woahPatchOffset = 0x14D76EF4
woahPatchValue = 'Oh shit!'.encode( 'ascii' )
woahPatchFormat = '<10s'

tierOneTechLearnOffset = 0x14C8E58C
tierOneTechLearnValue = 0x28
tierOneTechLearnFormat = '<B'

scriptOffsetInBinary = 0x13FD5809

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

mapItemFormat = '<BB'

mapItemOffsets = (
            0x13FDD564, 0x13FDD57A, 0x13FDD590, 0x13FDD596, 0x13FDD59C, 0x13FDD5B2, 0x13FDD5C8, 0x13FDDE88,
            0x13FDDE9E, 0x13FDE7B4, 0x13FDE7CA, 0x13FDE7E0, 0x13FDF0EC, 0x13FDF102, 0x13FDF118, 0x13FDF12E,
            0x13FE0348, 0x13FE035E, 0x13FE0374, 0x13FE038A, 0x13FE1598, 0x13FE2800, 0x13FE3134, 0x13FE314A,
            0x13FE43D8, 0x13FE43EE, 0x13FE43D8, 0x13FE43EE, 0x13FE5F28, 0x13FE5F3E, 0x13FE6860, 0x13FE6876,
            0x13FE688C, 0x13FE68A2, 0x13FE7188, 0x13FE719E, 0x13FE71B4, 0x13FE7AB4, 0x13FE7ACA, 0x13FE8D10,
            0x13FE8D26, 0x13FE9FDC, 0x13FE9FF2, 0x13FEA008, 0x13FEA01E, 0x13FEA034, 0x13FEA04A, 0x13FEA060,
            0x13FEA076, 0x13FEA08C, 0x13FEA0A2, 0x13FEA0B8, 0x13FEA0CE, 0x13FEA0E4, 0x13FEA0FA, 0x13FEA10E,
            0x13FEC444, 0x13FEC45A, 0x13FEC470, 0x13FECD64, 0x13FECD7A, 0x13FECD90, 0x13FED694, 0x13FED6AA,
            0x13FED6C0, 0x13FEDFC0, 0x13FEDFD6, 0x13FEDFEC, 0x13FEE002, 0x13FEE018, 0x13FEF230, 0x13FEF246,
            0x13FEF25C, 0x13FEF230, 0x13FEF246, 0x13FEF25C, 0x13FF72D0, 0x13FF72E6, 0x13FF72FC, 0x13FF7C00,
            0x13FF7C16, 0x13FF7C2C, 0x13FF7C42, 0x13FF852C, 0x13FF8542, 0x13FF8558, 0x13FF856E, 0x13FF8E68,
            0x13FF8E7E, 0x13FF8E94, 0x13FF8EAA, 0x13FF9794, 0x13FF8E7E, 0x13FF97C0, 0x13FF97D6, 0x13FFA9D8,
            0x13FFA9EE, 0x13FFAA04, 0x13FFAA1A, 0x13FFB320, 0x13FFB336, 0x13FFBC4C, 0x13FFBC62, 0x13FFBC78,
            0x13FFC584, 0x13FFC59A, 0x13FFCEA8, 0x13FFCEBE, 0x13FFCED4, 0x1400C6B4, 0x1400C6CA, 0x1400C6E0,
            0x1400CFEC, 0x1400D002, 0x1400D018, 0x1400D02E, 0x1400D920, 0x1400D936, 0x1400D94C, 0x1400E244,
            0x1400E25A, 0x1400E270, 0x1400EB9C, 0x1400EBB2, 0x1400EBC8, 0x1400EBDE, 0x1400FDE0, 0x1400FDF6,
            0x1400FE0C, 0x1400FE22, 0x14010700, 0x14010716, 0x14011030, 0x14011046, 0x1401105C, 0x14011072,
            0x14011968, 0x1401197E, 0x14012290, 0x140122A6, 0x140122BC, 0x140134F4, 0x1401350A, 0x14014758,
            0x1401476E, 0x14014784, 0x1401479A, 0x14015088, 0x1401509E, 0x140150B4, 0x140162E4, 0x140162FA,
            0x14016310, 0x14016326, 0x140190C8, 0x1401AC6C, 0x1401AC82, 0x1401AC98, 0x1401B594, 0x1401B5AA,
            0x1401BEC4, 0x1401BEDA, 0x1401BEF0, 0x1401C7FC, 0x1401C812, 0x1401C828, 0x1401DA60, 0x1401DA76,
            0x1401DA8C, 0x1401E388, 0x1401E39E, 0x1401E3B4, 0x1401ECB8, 0x1401ECCE, 0x1401ECE4, 0x1401ECFA,
            0x1401FF14, 0x1401FF2A, 0x140251D8, 0x1402B6FC, 0x1402B712, 0x1402B728, 0x1402C92C, 0x1402C942,
            0x1402C958, 0x1402C92C, 0x1402C942, 0x1402C958, 0x140312B8, 0x140312CE, 0x140312E4, 0x140312FA,
            0x14031BF4, 0x14031C0A, 0x14031C20, 0x14032530, 0x14032546, 0x1403255C, 0x14032572, 0x1403377C,
            0x14033792, 0x140337A8, 0x14034098, 0x140340AE, 0x140340C4, 0x140340DA, 0x14035C34, 0x14035C4A,
            0x14035C60, 0x14036578, 0x1403658E, 0x140365A4, 0x140365BA, 0x14039C8C, 0x14039CA2, 0x14010700,
            0x14010716, 0x1403C144, 0x1403C15A, 0x1403CA6C, 0x1403CA82, 0x1403DCD0, 0x1403E604, 0x140413F8,
            0x1404140E, 0x14041424, 0x1404143A, 0x14041D24, 0x14041D3A, 0x14041D50, 0x1407B3EA, 0x1407B400,
            0x1407B416, 0x1407B42C, 0x1407BD08, 0x1407BD0E, 0x1407BD14, 0x1407BD40
            )

recruitFormat = '<H'

#(if trigger list, trigger).  Starts with Jijimon conversation.
recruitOffsets = (
            ( ( 0x140B4572, 0x13FD893A, 0x13FD8A4A, 0x13FE503A, 0x13FE581A, 0x1402BBE6, 0x14059A40, 0x1405C40A,
                0x1405C6A2, 0x1405CA20, 0x1405CB42, 0x1405CD5C, 0x1405E044, 0x1405E222, 0x1405E344, 0x1405E420,
                0x1405E9B0, 0x14063CE2, 0x1406AB0A, 0x1406BC52, 0x1406D050, 0x1406D7E6 ),
              204 ), #Betamon
            #( ( 0x140B51F6, ), 205 ), #Greymon
            ( ( 0x140B6668, 0x13FD9634, 0x13FD9718, 0x13FE44A2, 0x1406D75C, 0x1406FE82, 0x140701D2 ),
              206 ), #Devimon
            ( ( 0x140B47C0, 0x13FD8FF6, 0x13FD9120, 0x13FD9198, 0x13FD92C2, 0x1406B3DE, 0x1406B784, 0x1406C646,
                0x1406C9E6, 0x140AD37A, 0x13FE505A, 0x13FE513E, 0x13FE5222, 0x13FE583A, 0x13FE591E, 0x13FE5A02,
                0x13FE5D52, 0x1402BC06, 0x1402BCEA, 0x1402BDCE, 0x1402C5CE, 0x1402C6B2, 0x1402C796, 0x14051FC6,
                0x1405218A, 0x140598A4, 0x14059A60, 0x14059B44, 0x14059C28, 0x1405BFAE, 0x1405C16A, 0x1405C24E,
                0x1405C5B6, 0x1405E9D0, 0x1405EAB4, 0x1405EB98, 0x140608B0, 0x14060994, 0x14060A78, 0x14063D02,
                0x14063DE6, 0x14063ECA, 0x1406AB2A, 0x1406AC0E, 0x1406ACF2, 0x1406BC72, 0x1406BD56, 0x1406BE3A,
                0x1406D070, 0x1406D154, 0x1406D238, 0x1406D806, 0x1406D8EA, 0x1406D9CE, 0x1406F14E ),
              208 ), #Tyrannomon
            ( ( 0x140B4880, 0x140BA15A, 0x140BA288, 0x13FD917C, 0x13FD92AA, 0x13FE5056, 0x13FE513A, 0x13FE521E,
                0x13FE5836, 0x13FE591A, 0x13FE59FE, 0x13FE5D4E, 0x1402BC02, 0x1402BCE6, 0x1402BDCA, 0x1402C5CA,
                0x1402C6AE, 0x1402C792, 0x14051FC2, 0x14052186, 0x140598A0, 0x14059A5C, 0x14059B40, 0x14059C24,
                0x1405BFAA, 0x1405C166, 0x1405C24A, 0x1405C5B2, 0x1405E9CC, 0x1406B2B2, 0x1406B6C2, 0x1405EAB0,
                0x1405EB94, 0x140608AC, 0x1406C516, 0x1406C910, 0x14060990, 0x14060A74, 0x14063CFE, 0x14063DE2,
                0x14063EC6, 0x1406AB26, 0x140AD31A, 0x1406AC0A, 0x1406ACEE, 0x1406BC6E, 0x1406BD52, 0x1406BE36,
                0x1406D06C, 0x1406D150, 0x1406D234, 0x1406D802, 0x1406D8E6, 0x1406D9CA, 0x1406F14A ),
              209 ), #Meramon
            ( (),
              210 ), #Seadramon -- does nothing in town and has no Jijimon message
            ( ( 0x140B5A62, 0x13FD95E0, 0x13FD96D0, 0x13FE44A6, 0x1406D760, 0x1406FC62, 0x1406FFC8 ),
              211 ), #Numemon
            ( ( 0x140B598E, 0x13FD9618, 0x13FD9700, 0x13FE44AE, 0x1406D764, 0x1406FDDC, 0x1407012E ),
              213 ), #Mamemon
            #( ( 0x140B644A, ), 214 ), #Monzaemon
            ( ( 0x140B563C, 0x13FD8F0C, 0x140672CE, 0x14067588 ),
              217 ), #Gabumon
            ( ( 0x140B4D44, 0x13FD89F0, 0x13FD8C72, 0x1405997A, 0x1405C4E6, 0x1405C556, 0x1405C56A, 0x1405C596,
                0x1405C5E2 ),
              218 ), #Elecmon
            ( ( 0x140B5B3A, 0x13FD7A70, 0x1402DBAC, 0x1402DE34, 0x1402E090, 0x1402E308, 0x1402E6BE, 0x1402E900 ),
              219 ), #Kabuterimon
            #( ( 0x140B54BA, ), 220 ), #Angemon
            #( ( 0x140B4BCE, ), 221 ), #Birdramon
            ( ( 0x140B4B26, 0x13FD9012, 0x13FD9138, 0x13FD91B4, 0x13FD92DA, 0x1406B4DA, 0x1406B880, 0x1406C742,
                0x1406CADA, 0x140AD3C6, 0x13FE505E, 0x13FE5142, 0x13FE5226, 0x13FE583E, 0x13FE5922, 0x13FE5A06,
                0x13FE5D56, 0x1402BC0A, 0x1402BCEE, 0x1402BDD2, 0x1402C5D2, 0x1402C6B6, 0x1402C79A, 0x14051FCA,
                0x1405218E, 0x140598A8, 0x14059A64, 0x14059B48, 0x14059C2C, 0x1405BFB2, 0x1405C16E, 0x1405C252,
                0x1405C5BA, 0x1405E9D4, 0x1405EAB8, 0x1405EB9C, 0x140608B4, 0x14060998, 0x14060A7C, 0x14063D06,
                0x14063DEA, 0x14063ECE, 0x1406AB2E, 0x1406AC12, 0x1406ACF6, 0x1406BC76, 0x1406BD5A, 0x1406BE3E,
                0x1406D074, 0x1406D158, 0x1406D23C, 0x1406D80A, 0x1406D8EE, 0x1406D9D2, 0x1406F152 ),
              222 ), #Garurumon
            ( ( 0x140B4A80, 0x13FD902E, 0x13FD9150, 0x13FD91D0, 0x13FD92F2, 0x1406B5E0, 0x1406B99A, 0x1406C844,
                0x1406CC16, 0x140AEEAA, 0x13FE5062, 0x13FE5146, 0x13FE522A, 0x13FE5842, 0x13FE5926, 0x13FE5A0A,
                0x13FE5D5A, 0x1402BC0E, 0x1402BCF2, 0x1402BDD6, 0x1402C5D6, 0x1402C6BA, 0x1402C79E, 0x14051FCE,
                0x14052192, 0x140598AC, 0x14059A68, 0x14059B4C, 0x14059C30, 0x1405BFB6, 0x1405C172, 0x1405C256,
                0x1405C5BE, 0x1405E9D8, 0x1405EABC, 0x1405EBA0, 0x140608B8, 0x1406099C, 0x14060A80, 0x14063D0A,
                0x14063DEE, 0x14063ED2, 0x1406AB32, 0x1406AC16, 0x1406ACFA, 0x1406BC7A, 0x1406BD5E, 0x1406BE42,
                0x1406D078, 0x1406D15C, 0x1406D240, 0x1406D80E, 0x1406D8F2, 0x1406D9D6, 0x1406F156 ),
              223 ), #Frigimon
            ( ( 0x140B57F4, 0x13FD86FC, 0x1405986C, 0x1405B1FE ),
              224 ), #Whamon
            #( ( 0x140B46F0, ), 225 ), #Vegiemon
            ( ( 0x140B68BE, ),
              226 ), #SkullGreymon  -- does nothing except tournament
            ( ( 0x140B617C, 0x13FD9982 ),
              227 ), #MetalMamemon
            ( ( 0x140B626E, 0x13FD904E, 0x13FD91F0, 0x140AEEEA ),
              228 ), #Vademon
            ( ( 0x140B507C, 0x13FD8946, 0x13FD8A56, 0x13FD8FA2, 0x13FD931E, 0x13FD9560, 0x13FE5016, 0x13FE57F6,
                0x1402BBC2, 0x140598D8, 0x14059A1C, 0x1405C3EA, 0x1405C6B0, 0x1405C972, 0x1405E98C, 0x14063CBE,
                0x1406AAE6, 0x1406BC2E, 0x1406D02C, 0x1406D7C2, 0x1406DADE, 0x1406E176, 0x1407056C, 0x14072670 ),
            231 ), #Patamon
            ( ( 0x140B432E, 0x13FD89B2, 0x13FD8CAE, 0x13FE438C, 0x13FE43B0, 0x13FE55F0, 0x13FE5614, 0x1405C50E,
                0x1405E4C6 ),
              232 ), #Kunemon
            ( ( 0x140B4FB8, 0x13FD894E, 0x13FD8A5E, 0x13FD8FAA, 0x13FD9356, 0x13FD9590, 0x13FE501E, 0x13FE57FE,
                0x1402BBCA, 0x140598E0, 0x14059A24, 0x1405C3F2, 0x1405C6B8, 0x1405C97A, 0x1405E994, 0x14063CC6,
                0x1406AAEE, 0x1406BC36, 0x1406D034, 0x1406D7CA, 0x1406DDC2, 0x1406E30A, 0x14070574, 0x14072678 ),
              233 ), #Unimon
            ( ( 0x140B5E82, 0x13FD8BD2, 0x13FF293A ),
              234 ), #Ogremon
            ( ( 0x140B4C64, 0x13FD898A, 0x13FD8BBE, 0x13FD8BF6, 0x1405C496, 0x1405C4EA, 0x1405E4A4 ),
              235 ), #Shellmon
            #( ( 0x140B43DC, ), 236 ), #Centarumon
            ( ( 0x140B462E, 0x13FD8970, 0x13FD8C4A ),
              237 ), #Bakemon
            ( ( 0x140B5568, 0x14059854, 0x1405B1E4 ),
              238 ), #Drimogemon
            ( ( 0x13FD87F6, ),
              239 ), #Sukamon -- no Jijimon
            ( ( 0x140B6990, 0x13FD8780 ),
              240 ), #Andromon
            ( ( 0x140B5DE0, 0x1405E514 ),
              241 ), #Giromon
            ( ( 0x140B60CE, 0x13FD63CA ),
              242 ), #Etemon
            ( ( 0x140B5132, 0x13FD894A, 0x13FD8A5A, 0x13FD8FA6, 0x13FD933A, 0x13FD9578, 0x13FE501A, 0x13FE57FA,
                0x1402BBC6, 0x140598DC, 0x14059A20, 0x1405C3EE, 0x1405C6B4, 0x1405C976, 0x1405E990, 0x14063CC2,
                0x1406AAEA, 0x1406BC32, 0x1406D030, 0x1406D7C6, 0x1406DC52, 0x1406E240, 0x14070570, 0x14072674 ),
              245 ), #Biyomon
            #( ( 0x140B4266, ), 246 ), #Palmon
            ( ( 0x140B4ED0, 0x13FD8952, 0x13FD8A62, 0x13FD8FAE, 0x13FD9372, 0x13FD95A8, 0x13FE5022, 0x13FE5802,
                0x1402BBCE, 0x140598E4, 0x14059A28, 0x1405C3F6, 0x1405C6BC, 0x1405C97E, 0x1405E998, 0x14063CCA,
                0x1406AAF2, 0x1406BC3A, 0x1406D7CE, 0x1406DF30, 0x1406E3BE, 0x14070578, 0x1407267C ),
              247 ), #Monochromon
            ( ( 0x140B5F30, 0x13FD8ED2 ),
              248 ), #Leomon
            ( ( 0x140B44C0, 0x13FD8FBA, 0x13FE503E, 0x13FE581E, 0x1402BBEA, 0x14059A44, 0x1405C5FE, 0x1405C612,
                0x1405C626, 0x1405C63A, 0x1405C64E, 0x1405C662, 0x1405C676, 0x1405C68A, 0x1405CA28, 0x1405CB46,
                0x1405CD60, 0x1405E03C, 0x1405E22A, 0x1405E348, 0x1405E424, 0x1405E47C, 0x1405E9B4, 0x14063CE6,
                0x1406AB0E, 0x1406BC56, 0x1406D054, 0x1406D7EA ),
              249 ), #Coelamon
            ( ( 0x140B4E06, 0x13FD873A, 0x13FD87C6, 0x14059908, 0x1405994A, ),
              250 ), #Kokatorimon
            ( ( 0x140B5D3C, 0x13FD7A82 ),
              251 ), #Kuwagamon
            ( ( 0x140B58A4, 0x13FD95FC, 0x13FD96E8, 0x13FE44AA, 0x1406D768, 0x1406FD28, 0x1407006E ),
              252 ), #Mojyamon
            ( ( 0x140B63C6, 0x13FD8F5A ),
              253 ), #Nanimon
            ( (),
              254 ), #Megadramon -- does nothing and has no Jijimon message
            ( ( 0x140B600A, 0x13FD9396 ),
              255 ), #Piximon
            ( ( 0x140B67EE, 0x13FD906E, 0x13FD9210, 0x140AEF36 ),
              256 ), #Digitamamon
            ( ( 0x140B53E6, 0x13FD999E, 0x14063218, 0x14063250, 0x14095A7E, 0x140632A4, ),
              257 ), #Penguinmon
            ( ( 0x140B573A, 0x13FD95CE, 0x13FE4494 ),
              258 )  #Ninjamon
            )

specEvoFormat = '<B'

specEvoOffsets = (
            ( ( 0x140466BF, 0x14046693, 0x14046841 ),
              0x0E ), #Monzaemon/Toy Town
            ( ( 0x14054503, ),
              0x29 ), #Giromon
            ( ( 0x14054589, ),
              0x1B ), #MetalMamemon
            ( ( 0x140A2E11, ),
              0x25 ), #Bakemon
            ( ( 0x140A2E5D, ),
              0x1A ), #SkullGreymon
            ( ( 0x140A2EA9, ),
              0x3B ), #Phoenixmon
            ( ( 0x140A2EFB, ),
              0x06 )  #Devimon
            )

tokoItemFormat = '<BxBB'

tokoItemOffsets = (
            0x14071064,
            0x14071068,
            0x1407106C,
            0x14071070,
            0x14071074,
            0x14071078,
            )

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

techDataFormat           = '<H7B5xBx'

techDataBlockOffset      = 0x14D66DF8
techDataBlockSize        = 0x8C0
techDataBlockCount       = 0x79

techDataExclusionOffsets = (
            0x14D673B8,
            )
techDataExclusionSize    = 0x130

techTierListFormat       = '<8B'

techTierListBlockOffset  = 0x14C8E554
techTierListBlockSize    = 0x38
techTierListBlockCount   = 0x07

techTierListExclusionOffsets = (    #no exclusions in this block since it is tiny
            )
techTierListExclusionSize= 0x130

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

evoToFromFormat          = '<11B'

evoToFromBlockOffset     = 0x14D6CE04       #start of evo to/from block
evoToFromBlockSize       = 0x3FB            #total number of bytes
evoToFromBlockCount      = 0x41

evoToFromExclusionOffsets = (
            0x14D6CF98, #in to Bakemon 3-4
            )
evoToFromExclusionSize = 0x130

itemDataFormat    = '<20sIHHb?2x'

itemDataBlockOffset     = 0x14D676C4       #start of item data block
itemDataBlockSize       = 0x1260           #total number of bytes
itemDataBlockCount      = 0x80             #number of item blocks

itemDataExclusionOffsets = (
            0x14D67CE8, #in Red Berry
            0x14D68618, #in Coral charm
            )
itemDataExclusionSize = 0x130

starterSetDigimonOffset  = ( 0x14D271C0, 0x14D271B8 )   #set digimon id
starterChkDigimonOffset  = ( 0x14CD1D24, 0x14CD1D44 )   #check digimon id to set tech
starterLearnTechOffset   = ( 0x14CD1D40, 0x14CD1D60 )   #tech to learn
starterEquipAnimOffset   = ( 0x14CD1D30, 0x14CD1D50 )   #animation to equip

