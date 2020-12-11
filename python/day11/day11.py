import pathlib
import copy

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    d = [x.strip() for x in f.read().strip().split('\n')]

EMPTY = 'L'
OCC = '#'
FLOOR = '.'
ADJ = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
]

class Lobby:
    def __init__(self, d, tolerance=4):
        self.d = copy.deepcopy(d)
        self.xmax = len(self.d[0]) - 1
        self.ymax = len(self.d) - 1
        self.tolerance = tolerance

    def __getitem__(self, coord):
        x, y = coord
        if 0 <= x <= self.xmax and 0 <= y <= self.ymax:
            return self.d[y][x]

    def find_stable(self):
        while True:
            oldmap = ''.join(self.d)
            self.next()
            if ''.join(self.d) == oldmap:
                break

    def next(self):
        newmap = []
        for y, row in enumerate(self.d):
            newmap.append(''.join([self.next_state((x, y)) for x, _ in enumerate(row)]))
        self.d = newmap

    def next_state(self, coord):
        if self[coord] == EMPTY:
            if self.count_adj(coord) == 0:
                return OCC
        elif self[coord] == OCC:
            if self.count_adj(coord) >= self.tolerance:
                return EMPTY
        return self[coord]

    def count_adj(self, coord):
        return sum(self[tuple(a+b for a,b in zip(coord, change))] == OCC for change in ADJ)


class Lobby2(Lobby):
    def count_adj(self, coord):
        adj = []
        for change in ADJ:
            newcoord = tuple(a+b for a,b in zip(coord, change))
            while self[newcoord] == FLOOR:
                newcoord = tuple(a+b for a,b in zip(newcoord, change))
            adj.append(self[newcoord])
        return adj.count(OCC), adj.count(EMPTY)


l = Lobby(d)
l.find_stable()
print(''.join(l.d).count(OCC))

l2 = Lobby2(d, tolerance=5)
l2.find_stable()
print(''.join(l2.d).count(OCC))
