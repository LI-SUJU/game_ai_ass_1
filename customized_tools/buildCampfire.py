from random import randint
from gdpc import geometry as geo
from gdpc import Block

def buildCampfire(ED, houseSTARTX, houseSTARTZ, z, floor, house):
    if house.isCampfire==True:
        randomness4fire = randint(4,6)
        geo.placeCuboid(ED, (houseSTARTX+randomness4fire, z-floor.floorHeight+1, houseSTARTZ+randomness4fire), (houseSTARTX+randomness4fire, z-floor.floorHeight+1, houseSTARTZ+randomness4fire), Block("minecraft:campfire[facing=north,lit=true]"))
        