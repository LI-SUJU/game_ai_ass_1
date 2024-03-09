from gdpc import geometry as geo
from gdpc import Block

def buildCarpet(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor):
    geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ+4), (houseENDX-4, z-floor.floorHeight+1, houseENDZ-4), Block("minecraft:gray_carpet"))
        