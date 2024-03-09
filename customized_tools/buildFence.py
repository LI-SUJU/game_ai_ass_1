from gdpc import geometry as geo
from gdpc import Block

def buildFence(ED, house, houseSTARTX, houseSTARTZ, houseENDX, houseENDZ, z, i):
    if i!=house.nfloors-1:
        print("Building fence...")
        for j in range(houseSTARTX-2, houseENDX+3):
            ED.placeBlock((j, z+1, houseSTARTZ-2), Block("minecraft:spruce_fence_gate[facing=south]"))
            ED.placeBlock((j, z+1, houseENDZ+2), Block("minecraft:spruce_fence_gate[facing=south]"))
        for j in range(houseSTARTZ-2, houseENDZ+3):
            ED.placeBlock((houseSTARTX-2, z+1, j), Block("minecraft:spruce_fence_gate[facing=east]"))
            ED.placeBlock((houseENDX+2, z+1, j), Block("minecraft:spruce_fence_gate[facing=east]"))      