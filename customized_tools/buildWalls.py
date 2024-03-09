from gdpc import geometry as geo
from gdpc import Block

def buildWalls (ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor):
    geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseSTARTZ), (houseENDX, z-1, houseSTARTZ), Block("minecraft:stripped_dark_oak_log"))
    geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseENDZ), (houseENDX, z-1, houseENDZ), Block("minecraft:stripped_dark_oak_log"))
    geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX, z-1, houseENDZ), Block("minecraft:stripped_dark_oak_log"))
    geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseSTARTZ), (houseENDX, z-1, houseENDZ), Block("minecraft:stripped_dark_oak_log"))
    geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX, z-1, houseSTARTZ), Block("minecraft:stripped_spruce_log"))
    geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseENDZ), (houseSTARTX, z-1, houseENDZ), Block("minecraft:stripped_spruce_log"))
    geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseSTARTZ), (houseENDX, z-1, houseSTARTZ), Block("minecraft:stripped_spruce_log"))
    geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseENDZ), (houseENDX, z-1, houseENDZ), Block("minecraft:stripped_spruce_log"))
