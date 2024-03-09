import random
from gdpc import geometry as geo
from gdpc import Block

def buildCeiling(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor):
    print("Building ceiling...")
    geo.placeCuboid(ED, (houseSTARTX-2, z, houseSTARTZ-2), (houseENDX+2, z, houseENDZ+2), Block("minecraft:stripped_spruce_log"))
    geo.placeCuboid(ED, (houseSTARTX-2, z, houseSTARTZ-2), (houseENDX+2, z, houseENDZ+2), Block("minecraft:stripped_spruce_log"))
    # build lanterns
    print("Building lanterns...")
    randomness = random.randint(4,10)
    geo.placeCuboid(ED, (floor.stairsEntranceStart[0]+randomness, floor.stairsEntranceStart[1]-1, floor.stairsEntranceStart[2]+randomness), (floor.stairsEntranceStart[0]+randomness, floor.stairsEntranceStart[1]-1, floor.stairsEntranceStart[2]+randomness),Block("minecraft:lantern"))
    