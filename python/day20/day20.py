import pathlib

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'test')
with open(filename) as f:
    parts = [x.strip() for x in f.read().strip().split('\n\n')]

class Puzzle:
    def __init__(self):
        self.tiles = []
        self.sides = {}

    def add(self, tile):
        tile = Tile(tile)
        self.tiles.append(tile)

    @property
    def sidelength(self):
        return int(len(self.tiles)**0.5)

    def cache_sides(self):
        self.sides = {}
        for tile in self.tiles:
            for side in tile.sides_any_orientation():
                if side in self.sides:
                    self.sides[side].append(tile.n)
                else:
                    self.sides[side] = [tile.n]


class Tile:
    def __init__(self, tile):
        self.tile, self.n = self.create(tile)

    def create(self, tile):
        lines = tile.splitlines()
        name = int(lines[0].split()[1].strip(':'))
        return lines[1:], name

    def show(self):
        return '\n'.join(self.tile)

    def sides(self):
        top = self.tile[0]
        bottom = self.tile[-1]
        left = ''.join(x[0] for x in self.tile)
        right = ''.join(x[-1] for x in self.tile)
        return top, bottom, left, right

    def sides_any_orientation(self):
        out = []
        for side in self.sides():
            out.append(side)
            out.append(side[::-1])
        return out

    def flip_h(self):
        self.tile = [row[::-1] for row in self.tile]

    def flip_v(self):
        self.tile = self.tile[::-1]

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


p = Puzzle()
for part in parts:
    p.add(part)
p.cache_sides()
print(p.sides)

t = p.tiles[0]
print(t.show())
print()
t.rotate()
print(t.show())

# print(p)
# print(p.tiles[0].tile)
# print(p.tiles[0].sides_any_orientation())
# print(p.sidelength)
