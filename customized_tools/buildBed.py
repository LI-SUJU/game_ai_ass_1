import random
from gdpc import geometry as geo
from gdpc import Block

def buildBed(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor):
    bed_side = random.choice(["south", "west"])# we don't want to build bed on the north side because of the stairs
    print(f"Building bed on the {bed_side} side...")
    if bed_side == "north":
        geo.placeCuboid(ED, (houseSTARTX+1, z-floor.floorHeight+1, houseSTARTZ+1), (houseSTARTX+1, z-floor.floorHeight+1, houseSTARTZ+1), Block("minecraft:black_bed"))
        # build bookshelf
        geo.placeCuboid(ED, (houseSTARTX+1, z-floor.floorHeight+1, houseSTARTZ+3), (houseSTARTX+1, z-floor.floorHeight+1, houseSTARTZ+3), Block("minecraft:bookshelf"))
    elif bed_side == "south":
        geo.placeCuboid(ED, (houseENDX-1, z-floor.floorHeight+1, houseENDZ-1), (houseENDX-1, z-floor.floorHeight+1, houseENDZ-1), Block("minecraft:black_bed"))
        # build bookshelf
        geo.placeCuboid(ED, (houseENDX-1, z-floor.floorHeight+1, houseENDZ-3), (houseENDX-1, z-floor.floorHeight+1, houseENDZ-3), Block("minecraft:bookshelf"))
    elif bed_side == "east":
        geo.placeCuboid(ED, (houseENDX-1, z-floor.floorHeight+1, houseSTARTZ+1), (houseENDX-1, z-floor.floorHeight+1, houseSTARTZ+1), Block("minecraft:black_bed"))
        # build bookshelf
        geo.placeCuboid(ED, (houseENDX-3, z-floor.floorHeight+1, houseSTARTZ+1), (houseENDX-3, z-floor.floorHeight+1, houseSTARTZ+1), Block("minecraft:bookshelf"))
    elif bed_side == "west":
        geo.placeCuboid(ED, (houseSTARTX+1, z-floor.floorHeight+1, houseENDZ-1), (houseSTARTX+1, z-floor.floorHeight+1, houseENDZ-1), Block("minecraft:black_bed"))
        # build bookshelf
        geo.placeCuboid(ED, (houseSTARTX+1, z-floor.floorHeight+1, houseENDZ-3), (houseSTARTX+1, z-floor.floorHeight+1, houseENDZ-3), Block("minecraft:bookshelf"))
        