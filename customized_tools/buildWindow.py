import random
from gdpc import geometry as geo
from gdpc import Block

def buildWindow(ED, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, floor, door_side, i):
    if i==0:
        choice_list = ["north", "south", "east", "west"]
        choice_list.remove(door_side)
        print(choice_list)
        window_side = random.choice(choice_list)
    else:
        window_side = random.choice(["north", "south", "east", "west"])
    print(f"Building windows on the {window_side} side...")
    randomness = random.randint(1,10-floor.windowWidth-1)
    # build windows
    if window_side == "north":
        geo.placeCuboid(ED, (houseSTARTX+randomness, z-floor.floorHeight+1, houseSTARTZ), (houseSTARTX+randomness+floor.windowWidth-1, z-floor.floorHeight+1+floor.windowHeight-1, houseSTARTZ), Block("minecraft:glass"))
    elif window_side == "south":
        geo.placeCuboid(ED, (houseENDX-randomness-floor.windowWidth, z-floor.floorHeight+1, houseENDZ), (houseENDX-randomness, z-floor.floorHeight+1+floor.windowHeight, houseENDZ), Block("minecraft:glass"))
    elif window_side == "east":
        geo.placeCuboid(ED, (houseENDX, z-floor.floorHeight+1, houseSTARTZ+randomness), (houseENDX, z-floor.floorHeight+1+floor.windowHeight, houseSTARTZ+randomness+floor.windowWidth), Block("minecraft:glass"))
    elif window_side == "west":
        geo.placeCuboid(ED, (houseSTARTX, z-floor.floorHeight+1, houseENDZ-randomness-floor.windowWidth), (houseSTARTX, z-floor.floorHeight+1+floor.windowHeight, houseENDZ-randomness), Block("minecraft:glass"))
        