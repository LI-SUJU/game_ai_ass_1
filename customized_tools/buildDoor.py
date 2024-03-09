import random
from gdpc import geometry as geo
from gdpc import Block

def buildDoor(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor, i):
    
    if i==0:
        print('Building door...')

        door_side = random.choice(["north", "south", "east", "west"])
        print(f"Building door on the {door_side} side...")
        if door_side == "north":
            # clear surrounding blocks
            geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ-2), (houseSTARTX+6, z-floor.floorHeight+4, houseSTARTZ+2), Block("air"))
            # build door
            geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX+6, z-floor.floorHeight+4, houseSTARTZ), Block("minecraft:birch_wood"))
            geo.placeCuboid(ED, (houseSTARTX+5, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX+5, z-floor.floorHeight+1, houseSTARTZ), Block("minecraft:oak_door[facing=north,half=lower]"))
            # build door step
            print("Building door step...")
            geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight, houseSTARTZ-2), (houseSTARTX+6, z-floor.floorHeight, houseSTARTZ-1), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight-1, houseSTARTZ-3), (houseSTARTX+6, z-floor.floorHeight-1, houseSTARTZ-2), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight-2, houseSTARTZ-4), (houseSTARTX+6, z-floor.floorHeight-2, houseSTARTZ-3), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight-3, houseSTARTZ-5), (houseSTARTX+6, z-floor.floorHeight-3, houseSTARTZ-4), Block("minecraft:stripped_oak_wood"))
            # build torch
            geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ-2), (houseSTARTX+4, z-floor.floorHeight+1, houseSTARTZ-2), Block("minecraft:torch"))
            geo.placeCuboid(ED, (houseSTARTX+6, z-floor.floorHeight+1, houseSTARTZ-2), (houseSTARTX+6, z-floor.floorHeight+1, houseSTARTZ-2), Block("minecraft:torch"))
            # build wall sign
            geo.placeCuboid(ED, (houseSTARTX+4, z-floor.floorHeight+2, houseSTARTZ-1), (houseSTARTX+4, z-floor.floorHeight+2, houseSTARTZ-1), Block("minecraft:dark_oak_wall_sign[facing=north]"))
        elif door_side == "south":
            geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight+1, houseENDZ-2), (houseENDX-6, z-floor.floorHeight+4, houseENDZ+2), Block("air"))
            geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight+1, houseENDZ), (houseENDX-6, z-floor.floorHeight+4, houseENDZ), Block("minecraft:birch_wood"))
            geo.placeCuboid(ED, (houseENDX-5, z-floor.floorHeight+1, houseENDZ), (houseENDX-5, z-floor.floorHeight+1, houseENDZ), Block("minecraft:oak_door[facing=south,half=lower]"))
            print("Building door step...")
            geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight, houseENDZ+1), (houseENDX-6, z-floor.floorHeight, houseENDZ+2), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight-1, houseENDZ+2), (houseENDX-6, z-floor.floorHeight-1, houseENDZ+3), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight-2, houseENDZ+3), (houseENDX-6, z-floor.floorHeight-2, houseENDZ+4), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight-3, houseENDZ+4), (houseENDX-6, z-floor.floorHeight-3, houseENDZ+5), Block("minecraft:stripped_oak_wood"))
            # build torch
            geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight+1, houseENDZ+1), (houseENDX-4, z-floor.floorHeight+1, houseENDZ+1), Block("minecraft:torch"))
            geo.placeCuboid(ED, (houseENDX-6, z-floor.floorHeight+1, houseENDZ+1), (houseENDX-6, z-floor.floorHeight+1, houseENDZ+1), Block("minecraft:torch"))
            # build wall sign
            geo.placeCuboid(ED, (houseENDX-4, z-floor.floorHeight+2, houseENDZ+1), (houseENDX-4, z-floor.floorHeight+2, houseENDZ+1), Block("minecraft:wall_sign[facing=south]"))
        elif door_side == "east":
            geo.placeCuboid(ED, (houseENDX-2, z-floor.floorHeight+1, houseENDZ-4), (houseENDX+2, z-floor.floorHeight+4, houseENDZ-6), Block("air"))
            # build door
            geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseENDZ-4), (houseENDX, z-floor.floorHeight+4, houseENDZ-6), Block("minecraft:birch_wood"))
            geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseENDZ-5), (houseENDX, z-floor.floorHeight+1, houseENDZ-5), Block("minecraft:oak_door[facing=east,half=lower]"))
            # build door step
            print("Building door step...")
            geo.placeCuboid(ED, (houseENDX+1, z-floor.floorHeight, houseENDZ-4), (houseENDX+2, z-floor.floorHeight, houseENDZ-6), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseENDX+2, z-floor.floorHeight-1, houseENDZ-4), (houseENDX+3, z-floor.floorHeight-1, houseENDZ-6), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseENDX+3, z-floor.floorHeight-2, houseENDZ-4), (houseENDX+4, z-floor.floorHeight-2, houseENDZ-6), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseENDX+4, z-floor.floorHeight-3, houseENDZ-4), (houseENDX+5, z-floor.floorHeight-3, houseENDZ-6), Block("minecraft:stripped_oak_wood"))
            # build torch
            geo.placeCuboid(ED, (houseENDX+2, z-floor.floorHeight+1, houseENDZ-4), (houseENDX+2, z-floor.floorHeight+1, houseENDZ-4), Block("minecraft:torch"))
            geo.placeCuboid(ED, (houseENDX+2, z-floor.floorHeight+1, houseENDZ-6), (houseENDX+2, z-floor.floorHeight+1, houseENDZ-6), Block("minecraft:torch"))
            # build wall sign
            geo.placeCuboid(ED, (houseENDX+1, z-floor.floorHeight+2, houseENDZ-4), (houseENDX+1, z-floor.floorHeight+2, houseENDZ-4), Block("minecraft:wall_sign[facing=east]{Text1:\""))
        elif door_side == "west":
            geo.placeCuboid(ED, (houseSTARTX-2, z-floor.floorHeight+1, houseSTARTZ+4), (houseSTARTX+2, z-floor.floorHeight+4, houseSTARTZ+6), Block("air"))
            geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseSTARTZ+4), (houseSTARTX, z-floor.floorHeight+4, houseSTARTZ+6), Block("minecraft:birch_wood"))
            geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseSTARTZ+5), (houseSTARTX, z-floor.floorHeight+1, houseSTARTZ+5), Block("minecraft:oak_door[facing=west,half=lower]"))
            print("Building door step...")
            geo.placeCuboid(ED, (houseSTARTX-2, z-floor.floorHeight, houseSTARTZ+4), (houseSTARTX-1, z-floor.floorHeight, houseSTARTZ+6), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseSTARTX-3, z-floor.floorHeight-1, houseSTARTZ+4), (houseSTARTX-2, z-floor.floorHeight-1, houseSTARTZ+6), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseSTARTX-4, z-floor.floorHeight-2, houseSTARTZ+4), (houseSTARTX-3, z-floor.floorHeight-2, houseSTARTZ+6), Block("minecraft:stripped_oak_wood"))
            geo.placeCuboid(ED, (houseSTARTX-5, z-floor.floorHeight-3, houseSTARTZ+4), (houseSTARTX-4, z-floor.floorHeight-3, houseSTARTZ+6), Block("minecraft:stripped_oak_wood"))
            # build torch
            geo.placeCuboid(ED, (houseSTARTX-2, z-floor.floorHeight+1, houseSTARTZ+4), (houseSTARTX-2, z-floor.floorHeight+1, houseSTARTZ+4), Block("minecraft:torch"))
            geo.placeCuboid(ED, (houseSTARTX-2, z-floor.floorHeight+1, houseSTARTZ+6), (houseSTARTX-2, z-floor.floorHeight+1, houseSTARTZ+6), Block("minecraft:torch"))
            # build wall sign
            geo.placeCuboid(ED, (houseSTARTX-1, z-floor.floorHeight+2, houseSTARTZ+6), (houseSTARTX-1, z-floor.floorHeight+2, houseSTARTZ+6), Block("minecraft:wall_sign[facing=west]"))
        return door_side