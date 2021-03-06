import pathlib
import copy
from itertools import count

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
        self.adj_cache = {}
        self.cache_adj()

    def __getitem__(self, coord):
        x, y = coord
        if 0 <= x <= self.xmax and 0 <= y <= self.ymax:
            return self.d[y][x]

    @property
    def flat(self):
        for y, row in enumerate(self.d):
            for x, ch in enumerate(row):
                yield ((x, y), ch)

    def cache_adj(self):
        for coord, ch in self.flat:
            self.adj_cache[coord] = []
            for change in ADJ:
                newcoord = tuple(a+b for a,b in zip(change, coord))
                if self[newcoord] not in [None, FLOOR]:
                    self.adj_cache[coord].append(newcoord)

    def find_stable(self):
        for i in count():
            oldmap = ''.join(ch for _, ch in self.flat)
            self.next()
            if ''.join(ch for _, ch in self.flat) == oldmap:
                break

    def next(self):
        newmap = []
        for y, row in enumerate(self.d):
            newmap.append([self.next_state((x, y)) for x, _ in enumerate(row)])
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
        return sum(self[newcoord] == OCC for newcoord in self.adj_cache[coord])


class Lobby2(Lobby):
    def cache_adj(self):
        for coord, ch in self.flat:
            self.adj_cache[coord] = []
            for change in ADJ:
                newcoord = tuple(a+b for a,b in zip(coord, change))
                while self[newcoord] == FLOOR:
                    newcoord = tuple(a+b for a,b in zip(newcoord, change))
                if self[newcoord] is not None:
                    self.adj_cache[coord].append(newcoord)

l = Lobby(d)
l.find_stable()
print(''.join(ch for _, ch in l.flat).count(OCC))

l2 = Lobby2(d, tolerance=5)
l2.find_stable()
print(''.join(ch for _, ch in l2.flat).count(OCC))
