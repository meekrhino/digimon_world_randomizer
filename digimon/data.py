# Author: Tristan Challener <challenert@gmail.com>
# Copyright: TODO

"""
Hard coded data values and binary offsets.
"""

rookies = [0x03, 0x04, 0x11, 0x12, 0x1F, 0x20, 0x2D, 0x2E, 0x39]

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

starter1SetDigimonOffset = 0x14D271B8
starter1ChkDigimonOffset = 0x14CD1D24
starter1LearnTechOffset  = 0x14CD1D40
starter1EquipAnimOffset  = 0x14CD1D30

starter2SetDigimonOffset = 0x14D271C0
starter2ChkDigimonOffset = 0x14CD1D44
starter2LearnTechOffset  = 0x14CD1D60
starter2EquipAnimOffset  = 0x14CD1D50


starter1DigimonIDOffsets = [starter1SetDigimonOffset, starter1ChkDigimonOffset]
starter2DigimonIDOffsets = [starter2SetDigimonOffset, starter2ChkDigimonOffset]
firstTechOffsets = [starter1LearnTechOffset]
secondTechOffsets = [starter2LearnTechOffset]
firstEquipOffsets = [starter1EquipAnimOffset]
secondEquipOffsets = [starter2EquipAnimOffset]