import random
from gdpc import geometry as geo
from gdpc import Block

def buildRoof(ED, house, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, i):
    if i==house.nfloors-1:

        geo.placeCuboid(ED, (houseSTARTX-2, z, houseSTARTZ-2), (houseENDX+2, z, houseENDZ+2), Block("minecraft:spruce_log"))
        # build roof
        if house.isRoof==True:
            print("Building roof...")
            geo.placeCuboid(ED, (houseSTARTX-1, z+1, houseSTARTZ-1), (houseENDX+1, z+1, houseENDZ+1), Block("minecraft:spruce_log"))
            geo.placeCuboid(ED, (houseSTARTX, z+2, houseSTARTZ), (houseENDX, z+2, houseENDZ), Block("minecraft:spruce_log"))
            geo.placeCuboid(ED, (houseSTARTX+1, z+3, houseSTARTZ+1), (houseENDX-1, z+3, houseENDZ-1), Block("minecraft:spruce_log"))
            geo.placeCuboid(ED, (houseSTARTX+2, z+4, houseSTARTZ+2), (houseENDX-2, z+4, houseENDZ-2), Block("minecraft:spruce_log"))
            geo.placeCuboid(ED, (houseSTARTX+3, z+5, houseSTARTZ+3), (houseENDX-3, z+5, houseENDZ-3), Block("minecraft:spruce_log"))
            geo.placeCuboid(ED, (houseSTARTX+4, z+6, houseSTARTZ+4), (houseENDX-4, z+6, houseENDZ-4), Block("minecraft:spruce_log"))
            print("roof built")
        