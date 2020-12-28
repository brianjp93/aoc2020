import pathlib
from collections import defaultdict
from functools import reduce
import copy
import re

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    parts = [x.strip() for x in f.read().strip().split('\n\n')]

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
MONSTER_STRING = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''.strip('\n')
MONSTER = []
for line in MONSTER_STRING.splitlines():
    row = [i for i, ch in enumerate(line) if ch == '#']
    MONSTER.append(row)
MONSTERLEN = 20
ADJ = ['rot'] * 3 + ['flip']

class Puzzle:
    def __init__(self):
        self.tiles = {}
        self.sides = {}
        self.map = {}

    def add(self, tile):
        tile = Tile(tile)
        self.tiles[tile.n] = tile

    def rotate(self, image, n=1):
        for i in range(n):
            out = []
            half = (len(image) - 1) / 2
            for y in range(len(image)):
                row = []
                for x in range(len(image[0])):
                    xn, yn = -(y - half), x - half
                    xn, yn = int(xn + half), int(yn + half)
                    row.append(image[yn][xn])
                out.append(''.join(row))
        return out

    def flip(self, image):
        return [x[::-1] for x in image]

    def find_monsters(self):
        edgeless = self.edgeless()
        line_len = MONSTERLEN
        count = 0
        i = 0
        while count == 0:
            if ADJ[i] == 'rot':
                edgeless = self.rotate(edgeless)
            else:
                edgeless = self.flip(edgeless)
            edgeless_copy = copy.deepcopy(edgeless)
            for y, row in enumerate(edgeless):
                for offset, ch in enumerate(row):
                    if offset + MONSTERLEN < len(row) and y+2 < len(edgeless):
                        if all(row[offset:offset+MONSTERLEN][x] == '#' for x in MONSTER[0]):
                            if all(edgeless[y+1][offset:offset+MONSTERLEN][x] == '#' for x in MONSTER[1]):
                                if all(edgeless[y+2][offset:offset+MONSTERLEN][x] == '#' for x in MONSTER[2]):
                                    for change in range(3):
                                        part = [x for x in edgeless_copy[y+change]]
                                        for n in MONSTER[change]:
                                            part[n+offset] = 'O'
                                        edgeless_copy[y+change] = ''.join(part)
                                    count += 1
            i = (i+1) % len(ADJ)
        return count, edgeless_copy

    def edgeless(self):
        if not self.map:
            self.create_map()
        minx = min(self.map.keys(), key=lambda x: x[0])[0]
        miny = min(self.map.keys(), key=lambda x: x[1])[1]
        maxx = max(self.map.keys(), key=lambda x: x[0])[0]
        maxy = max(self.map.keys(), key=lambda x: x[1])[1]
        out = []
        first = next(iter(self.tiles.values())).edgeless
        for y in range(miny, maxy+1):
            rows = [''] * len(first)
            for x in range(minx, maxx+1):
                tile = self.map[(x, y)]
                for i, row in enumerate(tile.edgeless):
                    rows[i] = rows[i] + row
            out = out + rows
        return out

    def cache_sides(self):
        self.sides = {}
        for tile in self.tiles.values():
            for side in tile.sides_any_orientation():
                if side in self.sides:
                    self.sides[side].append(tile.n)
                else:
                    self.sides[side] = [tile.n]

    def find_corners(self):
        count_single = defaultdict(int)
        for val in self.sides.values():
            if len(val) == 1:
                count_single[val[0]] += 1
        count_single = {key: val for key,val in count_single.items() if val == 4}
        return count_single

    def create_map(self):
        self.map[(0, 0)] = list(self.tiles.values())[0]
        while len(self.map) != len(self.tiles):
            currentmap = copy.deepcopy(self.map)
            for coord, tile in currentmap.items():
                for i, side in enumerate(tile.sides()):
                    nextcoord = tuple(a+b for a,b in zip(coord, DIRS[i]))
                    if nextcoord not in self.map:
                        if len(self.sides[side]) == 2:
                            for other in self.sides[side]:
                                if other != tile.n:
                                    othertile = self.tiles[other]
                                    while othertile.sides()[(i+2) % 4] != side:
                                        othertile.next()
                                    self.map[nextcoord] = othertile


class Tile:
    def __init__(self, tile):
        self.tile, self.n = self.create(tile)
        self.i = 0

    def create(self, tile):
        lines = tile.splitlines()
        name = int(lines[0].split()[1].strip(':'))
        return lines[1:], name

    @property
    def edgeless(self):
        return [x[1:-1] for x in self.tile[1:-1]]

    def sides(self):
        top = self.tile[0]
        bottom = self.tile[-1]
        left = ''.join(x[0] for x in self.tile)
        right = ''.join(x[-1] for x in self.tile)
        return top, right, bottom, left

    def sides_any_orientation(self):
        out = []
        for side in self.sides():
            out.append(side)
            out.append(side[::-1])
        return out

    def rotate(self):
        out = []
        half = (len(self.tile) - 1) / 2
        for y in range(len(self.tile)):
            row = []
            for x in range(len(self.tile[0])):
                xn, yn = -(y - half), x - half
                xn, yn = int(xn + half), int(yn + half)
                row.append(self.tile[yn][xn])
            out.append(''.join(row))
        self.tile = out

    def next(self):
        if ADJ[self.i] == 'rot':
            self.rotate()
        else:
            self.tile = self.tile[::-1]
        self.i = (self.i+1) % len(ADJ)


p = Puzzle()
for part in parts:
    p.add(part)
p.cache_sides()

singles = p.find_corners()
out = reduce(lambda x,y: x*y, singles.keys())
print(f'Part 1: {out}')

count, m = p.find_monsters()
roughness = ''.join(m).count('#')
print(f'Part 2: {roughness}')
