import logging
from random import randint
import random

from termcolor import colored

from gdpc import Block, Editor
from gdpc import geometry as geo
from gdpc import minecraft_tools as mt
from gdpc import editor_tools as et
from gdpc import vector_tools as vt
from customized_tools import terrain_scan_ex_water as tscan
from customized_tools.buildDoor import buildDoor
from customized_tools.buildCeiling import buildCeiling
from customized_tools.buildWindow import buildWindow
from customized_tools.buildCarpet import buildCarpet
from customized_tools.buildCampfire import buildCampfire
from customized_tools.buildStairs import buildStairs
from customized_tools.buildFence import buildFence
from customized_tools.buildWalls import buildWalls
from customized_tools.buildBed import buildBed
from customized_tools.buildRoof import buildRoof
# Here, we set up Python's logging system.
# GDPC sometimes logs some errors that it cannot otherwise handle.
logging.basicConfig(format=colored("%(name)s - %(levelname)s - %(message)s", color="yellow"))


# === STRUCTURE #2
# These variables are global and can be read from anywhere in the code.
# NOTE: If you want to change a global value inside one of your functions,
#       you'll have to add a line of code. For an example, search 'GLOBAL'.

# Here we construct an Editor object
ED = Editor(buffering=True)

# Here we read start and end coordinates of our build area
BUILD_AREA = ED.getBuildArea()  # BUILDAREA
STARTX, STARTY, STARTZ = BUILD_AREA.begin
LASTX, LASTY, LASTZ = BUILD_AREA.last

# WORLDSLICE
# Using the start and end coordinates we are generating a world slice
# It contains all manner of information, including heightmaps and biomes
# For further information on what information it contains, see
# https://minecraft.fandom.com/wiki/Chunk_format
#
# IMPORTANT: Keep in mind that a wold slice is a 'snapshot' of the world,
# and any changes you make later on will not be reflected in the world slice
WORLDSLICE = ED.loadWorldSlice(BUILD_AREA.toRect(), cache=True)  # this takes a while

# ROADHEIGHT = 0

# print("Calculating road height...")

heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
# Caclulating the average height along where we want to build our road
# xaxis = STARTX + (LASTX - STARTX) // 2  # Getting start + half the length
# zaxis = STARTZ + (LASTZ - STARTZ) // 2
# y = heights[(xaxis - STARTX, zaxis - STARTZ)]
# for x in range(STARTX, LASTX + 1):
#     newy = heights[(x - STARTX, zaxis - STARTZ)]
#     y = (y + newy) // 2
# for z in range(STARTZ, LASTZ + 1):
#     newy = heights[(xaxis - STARTX, z - STARTZ)]
#     y = (y + newy) // 2

#     # GLOBAL
#     # By calling 'global ROADHEIGHT' we allow writing to ROADHEIGHT.
#     # If 'global' is not called, a new, local variable is created.
# ROADHEIGHT = y
# print(f"Road height is {ROADHEIGHT}")
# === STRUCTURE #3
# Here we are defining all of our functions to keep our code organised
# They are:
# - buildPerimeter()
# - buildRoads()
# - buildCity()


def buildPerimeter():
    """Build a wall along the build area border.

    In this function we're building a simple wall around the build area
        pillar-by-pillar, which means we can adjust to the terrain height
    """
    # HEIGHTMAP
    # Heightmaps are an easy way to get the uppermost block at any coordinate
    # There are four types available in a world slice:
    # - 'WORLD_SURFACE': The top non-air blocks
    # - 'MOTION_BLOCKING': The top blocks with a hitbox or fluid
    # - 'MOTION_BLOCKING_NO_LEAVES': Like MOTION_BLOCKING but ignoring leaves
    # - 'OCEAN_FLOOR': The top solid blocks
    heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

    print("Building east-west walls...")

    for x in range(STARTX, LASTX + 1):
        # The northern wall
        y = heights[(x - STARTX, 0)]
        geo.placeCuboid(ED, (x, y - 2, STARTZ), (x, y, STARTZ), Block("granite"))
        geo.placeCuboid(ED, (x, y + 1, STARTZ), (x, y + 4, STARTZ), Block("granite_wall"))
        # The southern wall
        y = heights[(x - STARTX, LASTZ - STARTZ)]
        geo.placeCuboid(ED, (x, y - 2, LASTZ), (x, y, LASTZ), Block("red_sandstone"))
        geo.placeCuboid(ED, (x, y + 1, LASTZ), (x, y + 4, LASTZ), Block("red_sandstone_wall"))

    print("Building north-south walls...")

    for z in range(STARTZ, LASTZ + 1):
        # The western wall
        y = heights[(0, z - STARTZ)]
        geo.placeCuboid(ED, (STARTX, y - 2, z), (STARTX, y, z), Block("sandstone"))
        geo.placeCuboid(ED, (STARTX, y + 1, z), (STARTX, y + 4, z), Block("sandstone_wall"))
        # The eastern wall
        y = heights[(LASTX - STARTX, z - STARTZ)]
        geo.placeCuboid(ED, (LASTX, y - 2, z), (LASTX, y, z), Block("prismarine"))
        geo.placeCuboid(ED, (LASTX, y + 1, z), (LASTX, y + 4, z), Block("prismarine_wall"))


def buildRoads():
    """Build a road from north to south and east to west."""
    xaxis = STARTX + (LASTX - STARTX) // 2  # Getting start + half the length
    zaxis = STARTZ + (LASTZ - STARTZ) // 2
    heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]

    print("Calculating road height...")
    # Caclulating the average height along where we want to build our road
    y = heights[(xaxis - STARTX, zaxis - STARTZ)]
    for x in range(STARTX, LASTX + 1):
        newy = heights[(x - STARTX, zaxis - STARTZ)]
        y = (y + newy) // 2
    for z in range(STARTZ, LASTZ + 1):
        newy = heights[(xaxis - STARTX, z - STARTZ)]
        y = (y + newy) // 2

    # GLOBAL
    # By calling 'global ROADHEIGHT' we allow writing to ROADHEIGHT.
    # If 'global' is not called, a new, local variable is created.
    global ROADHEIGHT
    ROADHEIGHT = y

    print("Building east-west road...")

    geo.placeCuboid(ED, (xaxis - 2, y, STARTZ), (xaxis - 2, y, LASTZ), Block("end_stone_bricks"))
    geo.placeCuboid(ED, (xaxis - 1, y, STARTZ), (xaxis + 1, y, LASTZ), Block("gold_block"))
    geo.placeCuboid(ED, (xaxis + 2, y, STARTZ), (xaxis + 2, y, LASTZ), Block("end_stone_bricks"))
    geo.placeCuboid(ED, (xaxis - 1, y + 1, STARTZ), (xaxis + 1, y + 3, LASTZ), Block("air"))

    print("Building north-south road...")

    geo.placeCuboid(ED, (STARTX, y, zaxis - 2), (LASTX, y, zaxis - 2), Block("end_stone_bricks"))
    geo.placeCuboid(ED, (STARTX, y, zaxis - 1), (LASTX, y, zaxis + 1), Block("gold_block"))
    geo.placeCuboid(ED, (STARTX, y, zaxis + 2), (LASTX, y, zaxis + 2), Block("end_stone_bricks"))
    geo.placeCuboid(ED, (STARTX, y + 1, zaxis - 1), (LASTX, y + 3, zaxis + 1), Block("air"))

def buildPlatform():
    print("Building platform...")
    #get the highest point in an area

    house_area_STARTX, houseplatformSTARTY, house_area_STARTZ, decision = tscan.scanTerrain(area=BUILD_AREA, househeight=10, housewidth=16, houselength=16)
    if decision == True:

        platformSTARTX=house_area_STARTX+3
        platformSTARTZ=house_area_STARTZ+3
        highestHeight = 0
        # platformSTARTX=randint(STARTX, LASTX-10)
        # platformSTARTZ=randint(STARTZ, LASTZ-10)
        print(f"Platform start: {platformSTARTX}, {platformSTARTZ}")
        # WORLDSLICE = ED.loadWorldSlice(vt.Rect((platformSTARTX,platformSTARTZ),(10,10)), cache=True)  # this takes a while
        heights = WORLDSLICE.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
        for x in range(platformSTARTX, platformSTARTX+10):
            for z in range(platformSTARTZ, platformSTARTZ+10):
                y = heights[(x - platformSTARTX, z - platformSTARTZ)]
                if y > highestHeight:
                    highestHeight = y
        print(f"Highest point: {highestHeight}")
        print("Building north-south walls...")
        for x in range(platformSTARTX, platformSTARTX + 10):
            # The northern wall
            y = heights[(x - platformSTARTX, 0)]
            geo.placeCuboid(ED, (x, y - 2, platformSTARTZ), (x, y, platformSTARTZ), Block("granite"))
            geo.placeCuboid(ED, (x, y + 1, platformSTARTZ), (x, highestHeight, platformSTARTZ), Block("granite_wall"))
            # The southern wall
            y = heights[(x - platformSTARTX, 10)]
            geo.placeCuboid(ED, (x, y - 2, platformSTARTZ+10), (x, y, platformSTARTZ+10), Block("red_sandstone"))
            geo.placeCuboid(ED, (x, y + 1, platformSTARTZ+10), (x, highestHeight, platformSTARTZ+10), Block("red_sandstone_wall"))

        print("Building east-west walls...")

        for z in range(platformSTARTZ, platformSTARTZ + 10):
            # The western wall
            y = heights[(0, z - platformSTARTZ)]
            geo.placeCuboid(ED, (platformSTARTX, y - 2, z), (platformSTARTX, y, z), Block("sandstone"))
            geo.placeCuboid(ED, (platformSTARTX, y + 1, z), (platformSTARTX, highestHeight, z), Block("sandstone_wall"))
            # The eastern wall
            y = heights[(10, z - platformSTARTZ)]
            geo.placeCuboid(ED, (platformSTARTX+10, y - 2, z), (platformSTARTX+10, y, z), Block("prismarine"))
            geo.placeCuboid(ED, (platformSTARTX+10, y + 1, z), (platformSTARTX+10, highestHeight, z), Block("prismarine_wall"))
        # corner1 = (platformSTARTX, heights[(0,0)], platformSTARTZ)
        base1 = (platformSTARTX, highestHeight, platformSTARTZ)
        # corner2 = (platformSTARTX+10, heights[(10,10)], platformSTARTZ+50)
        base2 = (platformSTARTX+10, highestHeight, platformSTARTZ+10)
        # corner3 = (platformSTARTX+10, heights[(10,0)], platformSTARTZ)
        # base3 = (platformSTARTX+10, highestHeight+1, platformSTARTZ)
        # corner4 = (platformSTARTX, heights[(0,10)], platformSTARTZ+10)
        # base4 = (platformSTARTX, highestHeight+1, platformSTARTZ+10)
        # geo.placeCuboid(ED, corner1, base1, Block("stone"))
        # geo.placeCuboid(ED, corner2, base2, Block("stone"))
        # geo.placeCuboid(ED, corner3, base3, Block("stone"))
        # geo.placeCuboid(ED, corner4, base4, Block("stone"))
        # clear space above the platform for 10 blocks
        # geo.placeCuboid(ED, (house_area_STARTX, highestHeight+1, house_area_STARTZ), (house_area_STARTX+16, highestHeight+10, house_area_STARTZ+16), Block("air"))
        
        geo.placeCuboid(ED, base1, base2, Block("stone"))
        # geo.placeCuboid(ED, base2, base1, Block("stone"))
        # build fence
        # print("Building fence...")
        # for i in range(house_area_STARTX, house_area_STARTX+16):
        #     geo.placeCuboid(ED, (i, heights[i-house_area_STARTX,0], house_area_STARTZ),(i, highestHeight+1, house_area_STARTZ), Block("minecraft:spruce_fence_gate"))
        #     geo.placeCuboid(ED, (i, heights[i-house_area_STARTX,16], house_area_STARTZ+16),(i, highestHeight+1, house_area_STARTZ+16), Block("minecraft:spruce_fence_gate"))
        # for i in range(house_area_STARTZ, house_area_STARTZ+16):
        #     geo.placeCuboid(ED, (house_area_STARTX, heights[0,i-house_area_STARTZ], i),(house_area_STARTX, highestHeight+1, i), Block("minecraft:spruce_fence_gate", {"facing": "east"}))
        #     geo.placeCuboid(ED, (house_area_STARTX+16, heights[16,i-house_area_STARTZ], i),(house_area_STARTX+16, highestHeight+1, i), Block("minecraft:spruce_fence_gate", {"facing": "east"}))
        # print("fence built")
        print("Building house...")
        buildHouse(platformSTARTX, platformSTARTZ, highestHeight)
    else:
        print("No suitable area for building platform found. Please use another area.")

def buildHouse(x,z, highestHeight):
    houseSTARTX=x
    houseSTARTZ=z
    houseENDX=x+10
    houseENDZ=z+10
    # house properties
    class House:
        nfloors = randint(1, 5)
        isRoof = random.choice([True, False])
        isCampfire = random.choice([True, False])
    house= House()
    house.isRoof=False
    house.isCampfire=True
    print(f"Building house with {house.nfloors} floors...")
    for i in range(house.nfloors):
        print(f"Building floor {i+1}...")
        class Floor: 
            def __init__(self) :
                self.nthFloor= i+1
                self.floorHeight= 10
                self.windowWidth=randint(2, 4)
                self.windowHeight= randint(3, 5)
                self.windowStart= (random.choice([houseSTARTX, houseENDX]), randint(1,10),random.choice([houseSTARTZ, houseENDZ]))
                self.stairsEntranceStart= (0,0,0)
                pass
        floor= Floor()
        z=highestHeight+floor.floorHeight*floor.nthFloor
        floor.stairsEntranceStart= (houseSTARTX+1, z, houseSTARTZ+1)

        # geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseSTARTZ), (houseENDX, z-1, houseSTARTZ), Block("minecraft:stripped_dark_oak_log"))
        # geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseENDZ), (houseENDX, z-1, houseENDZ), Block("minecraft:stripped_dark_oak_log"))
        # geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX, z-1, houseENDZ), Block("minecraft:stripped_dark_oak_log"))
        # geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseSTARTZ), (houseENDX, z-1, houseENDZ), Block("minecraft:stripped_dark_oak_log"))
        # geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX, z-1, houseSTARTZ), Block("minecraft:stripped_spruce_log"))
        # geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseENDZ), (houseSTARTX, z-1, houseENDZ), Block("minecraft:stripped_spruce_log"))
        # geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseSTARTZ), (houseENDX, z-1, houseSTARTZ), Block("minecraft:stripped_spruce_log"))
        # geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseENDZ), (houseENDX, z-1, houseENDZ), Block("minecraft:stripped_spruce_log"))

        #build walls
        buildWalls(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor)
        # build fence
        buildFence(ED, house, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, i)
        # build door
        # build door in the first floor
        door_side = buildDoor(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor, i)
        # build ceiling
        buildCeiling(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor)
        #build windows
        buildWindow(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor, door_side, i)
        # build carpet
        buildCarpet(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor)
        # build campfire
        buildCampfire(ED, houseSTARTX, houseSTARTZ, z, floor, house)
        #build stairs
        buildStairs(ED, house, floor, i)
        # build bed
        buildBed(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor)
        # build roof
        buildRoof(ED, house, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, i)
        # if i!=house.nfloors-1:
        #     print("Building fence...")
        #     for j in range(houseSTARTX-2, houseENDX+3):
        #         ED.placeBlock((j, z+1, houseSTARTZ-2), Block("minecraft:spruce_fence_gate[facing=south]"))
        #         ED.placeBlock((j, z+1, houseENDZ+2), Block("minecraft:spruce_fence_gate[facing=south]"))
        #     for j in range(houseSTARTZ-2, houseENDZ+3):
        #         ED.placeBlock((houseSTARTX-2, z+1, j), Block("minecraft:spruce_fence_gate[facing=east]"))
        #         ED.placeBlock((houseENDX+2, z+1, j), Block("minecraft:spruce_fence_gate[facing=east]"))

            # which side of the house to build door
            # door_side = random.choice(["north", "south", "east", "west"])
            # door_side = "north"
            # print(f"Building door on the {door_side} side...")
            # if door_side == "north":
            #     # clear surrounding blocks
            #     geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ-2), (houseSTARTX+6, z-floor.floorHeight+4, houseSTARTZ+2), Block("air"))
            #     # build door
            #     geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX+6, z-floor.floorHeight+4, houseSTARTZ), Block("minecraft:birch_wood"))
            #     geo.placeCuboid(ED, (houseSTARTX+5, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX+5, z-floor.floorHeight+1, houseSTARTZ), Block("minecraft:oak_door[facing=north,half=lower]"))
            #     # build door step
            #     print("Building door step...")
            #     geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight, houseSTARTZ-2), (houseSTARTX+6, z-floor.floorHeight, houseSTARTZ-1), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight-1, houseSTARTZ-3), (houseSTARTX+6, z-floor.floorHeight-1, houseSTARTZ-2), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight-2, houseSTARTZ-4), (houseSTARTX+6, z-floor.floorHeight-2, houseSTARTZ-3), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight-3, houseSTARTZ-5), (houseSTARTX+6, z-floor.floorHeight-3, houseSTARTZ-4), Block("minecraft:stripped_oak_wood"))
            #     # build torch
            #     geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ-2), (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ-2), Block("minecraft:torch"))
            #     geo.placeCuboid(ED, (houseSTARTX+6, z-floor.floorHeight+1, houseSTARTZ-2), (houseSTARTX+6, z-floor.floorHeight+1, houseSTARTZ-2), Block("minecraft:torch"))
            # elif door_side == "south":
            #     geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight+2, houseENDZ-2), (houseENDX-6, z-floor.floorHeight+5, houseENDZ+2), Block("air"))
            #     geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight+2, houseENDZ), (houseENDX-6, z-floor.floorHeight+5, houseENDZ), Block("minecraft:birch_wood"))
            #     geo.placeCuboid(ED, (houseENDX-5, z-floor.floorHeight+2, houseENDZ), (houseENDX-5, z-floor.floorHeight+3, houseENDZ), Block("minecraft:oak_door[facing=south,half=lower]"))

            #     print("Building door step...")
            #     geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight, houseENDZ-2), (houseENDX-6, z-floor.floorHeight, houseENDZ-1), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight-1, houseENDZ-3), (houseENDX-6, z-floor.floorHeight-1, houseENDZ-2), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight-2, houseENDZ-4), (houseENDX-6, z-floor.floorHeight-2, houseENDZ-3), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight-3, houseENDZ-5), (houseENDX-6, z-floor.floorHeight-3, houseENDZ-4), Block("minecraft:stripped_oak_wood"))
            #     # build torch
            #     geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight+1, houseENDZ-2), (houseENDX-4, z-floor.floorHeight+1, houseENDZ-2), Block("minecraft:torch"))
            #     geo.placeCuboid(ED, (houseENDX-6, z-floor.floorHeight+1, houseENDZ-2), (houseENDX-6, z-floor.floorHeight+1, houseENDZ-2), Block("minecraft:torch"))
            # elif door_side == "east":
            #     geo.placeCuboid(ED, (houseENDX-2, z-floor.floorHeight+2, houseENDZ-4), (houseENDX+2, z-floor.floorHeight+5, houseENDZ-6), Block("air"))
            #     # build door
            #     geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+2, houseENDZ-4), (houseENDX, z-floor.floorHeight+5, houseENDZ-6), Block("minecraft:birch_wood"))
            #     geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+2, houseENDZ-5), (houseENDX, z-floor.floorHeight+3, houseENDZ-5), Block("minecraft:oak_door[facing=east,half=lower]"))
            #     # build door step
            #     print("Building door step...")
            #     geo.placeCuboid(ED, (houseENDX+1, z-floor.floorHeight, houseENDZ-4), (houseENDX+2, z-floor.floorHeight, houseENDZ-6), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseENDX+2, z-floor.floorHeight-1, houseENDZ-4), (houseENDX+3, z-floor.floorHeight-1, houseENDZ-6), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseENDX+3, z-floor.floorHeight-2, houseENDZ-4), (houseENDX+4, z-floor.floorHeight-2, houseENDZ-6), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseENDX+4, z-floor.floorHeight-3, houseENDZ-4), (houseENDX+5, z-floor.floorHeight-3, houseENDZ-6), Block("minecraft:stripped_oak_wood"))
            #     # build torch
            #     geo.placeCuboid(ED, (houseENDX+2, z-floor.floorHeight+1, houseENDZ-4), (houseENDX+2, z-floor.floorHeight+1, houseENDZ-4), Block("minecraft:torch"))
            #     geo.placeCuboid(ED, (houseENDX+2, z-floor.floorHeight+1, houseENDZ-6), (houseENDX+2, z-floor.floorHeight+1, houseENDZ-6), Block("minecraft:torch"))
            # elif door_side == "west":
            #     geo.placeCuboid(ED, (houseSTARTX-2, z-floor.floorHeight+2, houseSTARTZ+4), (houseSTARTX+2, z-floor.floorHeight+5, houseSTARTZ+6), Block("air"))
            #     geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+2, houseSTARTZ+4), (houseSTARTX, z-floor.floorHeight+5, houseSTARTZ+6), Block("minecraft:birch_wood"))
            #     geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+2, houseSTARTZ+5), (houseSTARTX, z-floor.floorHeight+3, houseSTARTZ+5), Block("minecraft:oak_door[facing=west,half=lower]"))

            #     print("Building door step...")
            #     geo.placeCuboid(ED, (houseSTARTX-2, z-floor.floorHeight, houseSTARTZ+4), (houseSTARTX-1, z-floor.floorHeight, houseSTARTZ+6), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseSTARTX-3, z-floor.floorHeight-1, houseSTARTZ+4), (houseSTARTX-2, z-floor.floorHeight-1, houseSTARTZ+6), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseSTARTX-4, z-floor.floorHeight-2, houseSTARTZ+4), (houseSTARTX-3, z-floor.floorHeight-2, houseSTARTZ+6), Block("minecraft:stripped_oak_wood"))
            #     geo.placeCuboid(ED, (houseSTARTX-5, z-floor.floorHeight-3, houseSTARTZ+4), (houseSTARTX-4, z-floor.floorHeight-3, houseSTARTZ+6), Block("minecraft:stripped_oak_wood"))
            #     # build torch
            #     geo.placeCuboid(ED, (houseSTARTX-2, z-floor.floorHeight+1, houseSTARTZ+4), (houseSTARTX-2, z-floor.floorHeight+1, houseSTARTZ+4), Block("minecraft:torch"))
            #     geo.placeCuboid(ED, (houseSTARTX-2, z-floor.floorHeight+1, houseSTARTZ+6), (houseSTARTX-2, z-floor.floorHeight+1, houseSTARTZ+6), Block("minecraft:torch"))
        
        # geo.placeCuboid(ED, (houseSTARTX-2, z, houseSTARTZ-2), (houseENDX+2, z, houseENDZ+2), Block("minecraft:stripped_spruce_log"))

        # which side of the house to build windows
        # if i==0:
        #     choice_list = ["north", "south", "east", "west"]
        #     choice_list.remove(door_side)
        #     print(choice_list)
        #     window_side = random.choice(choice_list)
        # else:
        #     window_side = random.choice(["north", "south", "east", "west"])
        # print(f"Building windows on the {window_side} side...")
        # randomness = randint(1,10-floor.windowWidth-1)
        # # build windows
        # if window_side == "north":
            
        #     geo.placeCuboid(ED, (houseSTARTX+randomness, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX+randomness+floor.windowWidth, z-floor.floorHeight+1+floor.windowHeight, houseSTARTZ), Block("minecraft:glass"))
        # elif window_side == "south":
        #     geo.placeCuboid(ED, (houseENDX-randomness-floor.windowWidth, z-floor.floorHeight+1, houseENDZ), (houseENDX-randomness, z-floor.floorHeight+1+floor.windowHeight, houseENDZ), Block("minecraft:glass"))
        # elif window_side == "east":
        #     geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseSTARTZ+randomness), (houseENDX, z-floor.floorHeight+1+floor.windowHeight, houseSTARTZ+randomness+floor.windowWidth), Block("minecraft:glass"))
        # elif window_side == "west":
        #     geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseENDZ-randomness-floor.windowWidth), (houseSTARTX, z-floor.floorHeight+1+floor.windowHeight, houseENDZ-randomness), Block("minecraft:glass"))

        # geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ+4), (houseENDX-4, z-floor.floorHeight+1, houseENDZ-4), Block("minecraft:gray_carpet"))

        # randomness4fire = randint(4,6)
        # geo.placeCuboid(ED, (houseSTARTX+randomness4fire, z-floor.floorHeight+1, houseSTARTZ+randomness4fire), (houseSTARTX+randomness4fire, z-floor.floorHeight+1, houseSTARTZ+randomness4fire), Block("minecraft:campfire[facing=north,lit=true]"))

        # if i!=house.nfloors-1:
        #     geo.placeCuboid(ED, floor.stairsEntranceStart, (floor.stairsEntranceStart[0]+2, floor.stairsEntranceStart[1], floor.stairsEntranceStart[2]+2), Block("air"))
        #     for _ in range(1,10):
        #         geo.placeCuboid(ED, (floor.stairsEntranceStart[0]+_-1, floor.stairsEntranceStart[1]-_, floor.stairsEntranceStart[2]), (floor.stairsEntranceStart[0]+_-1, floor.stairsEntranceStart[1]-_, floor.stairsEntranceStart[2]+2), Block("minecraft:polished_andesite"))
        

        # bed_side = random.choice(["south", "west"])# we don't want to build bed on the north side because of the stairs
        # print(f"Building bed on the {bed_side} side...")
        # if bed_side == "north":
        #     geo.placeCuboid(ED, (houseSTARTX+1, z-floor.floorHeight+1, houseSTARTZ+1), (houseSTARTX+1, z-floor.floorHeight+1, houseSTARTZ+1), Block("minecraft:black_bed"))
        # elif bed_side == "south":
        #     geo.placeCuboid(ED, (houseENDX-1, z-floor.floorHeight+1, houseENDZ-1), (houseENDX-1, z-floor.floorHeight+1, houseENDZ-1), Block("minecraft:black_bed"))
        # elif bed_side == "east":
        #     geo.placeCuboid(ED, (houseENDX-1, z-floor.floorHeight+1, houseSTARTZ+1), (houseENDX-1, z-floor.floorHeight+1, houseSTARTZ+1), Block("minecraft:black_bed"))
        # elif bed_side == "west":
        #     geo.placeCuboid(ED, (houseSTARTX+1, z-floor.floorHeight+1, houseENDZ-1), (houseSTARTX+1, z-floor.floorHeight+1, houseENDZ-1), Block("minecraft:black_bed"))

        # if i==house.nfloors-1:
        #     # build roof
        #     print("Building roof...")
        #     geo.placeCuboid(ED, (houseSTARTX-2, z, houseSTARTZ-2), (houseENDX+2, z, houseENDZ+2), Block("minecraft:spruce_log"))
        #     geo.placeCuboid(ED, (houseSTARTX-1, z+1, houseSTARTZ-1), (houseENDX+1, z+1, houseENDZ+1), Block("minecraft:spruce_log"))
        #     geo.placeCuboid(ED, (houseSTARTX, z+2, houseSTARTZ), (houseENDX, z+2, houseENDZ), Block("minecraft:spruce_log"))
        #     geo.placeCuboid(ED, (houseSTARTX+1, z+3, houseSTARTZ+1), (houseENDX-1, z+3, houseENDZ-1), Block("minecraft:spruce_log"))
        #     geo.placeCuboid(ED, (houseSTARTX+2, z+4, houseSTARTZ+2), (houseENDX-2, z+4, houseENDZ-2), Block("minecraft:spruce_log"))
        #     geo.placeCuboid(ED, (houseSTARTX+3, z+5, houseSTARTZ+3), (houseENDX-3, z+5, houseENDZ-3), Block("minecraft:spruce_log"))
        #     geo.placeCuboid(ED, (houseSTARTX+4, z+6, houseSTARTZ+4), (houseENDX-4, z+6, houseENDZ-4), Block("minecraft:spruce_log"))
        #     print("roof built")
        print(f"floor {i+1} built")
def main():
    try:
        # buildPerimeter()
        # buildRoads()
        buildPlatform()
        print("Done!")

    except KeyboardInterrupt: # useful for aborting a run-away program
        print("Pressed Ctrl-C to kill program.")


# === STRUCTURE #4
# The code in here will only run if we run the file directly (not imported).
# This prevents people from accidentally running your generator.
# It is recommended to directly call a function here, because any variables
# you declare outside a function will be global.
if __name__ == '__main__':
    main()