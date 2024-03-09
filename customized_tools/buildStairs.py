from gdpc import geometry as geo
from gdpc import Block

def buildStairs(ED, house, floor, i):
    if i!=house.nfloors-1:
        geo.placeCuboid(ED, floor.stairsEntranceStart, (floor.stairsEntranceStart[0]+2, floor.stairsEntranceStart[1], floor.stairsEntranceStart[2]+2), Block("air"))
        for _ in range(1,10):
            geo.placeCuboid(ED, (floor.stairsEntranceStart[0]+_-1, floor.stairsEntranceStart[1]-_, floor.stairsEntranceStart[2]), (floor.stairsEntranceStart[0]+_-1, floor.stairsEntranceStart[1]-_, floor.stairsEntranceStart[2]+2), Block("minecraft:polished_andesite"))