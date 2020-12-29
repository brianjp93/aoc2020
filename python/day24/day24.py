import pathlib
import re
from collections import defaultdict

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    data = [x.strip() for x in f.read().strip().split('\n')]


ADJ = {
    'nw': (-1, 1),
    'ne': (1, 1),
    'w': (-2, 0),
    'e': (2, 0),
    'sw': (-1, -1),
    'se': (1, -1),
}


class Room:
    def __init__(self, init=None):
        self.map = init if init else set()
        self.get_relevant()

    def get_adj(self, coord):
        for change in ADJ.values():
            yield tuple(a+b for a, b in zip(coord, change))

    def get_relevant(self):
        rel = defaultdict(int)
        for coord in self.map:
            for other in self.get_adj(coord):
                rel[other] += 1
        self.rel = rel

    def next(self):
        nmap = set()
        nrel = defaultdict(int)
        for coord, black in self.rel.items():
            if black == 2 or black == 1 and coord in self.map:
                nmap.add(coord)
                for other in self.get_adj(coord):
                    nrel[other] += 1
        self.rel = nrel
        self.map = nmap

    def cycle(self, i):
        for _ in range(i):
            self.next()


def simplify(path):
    directions = re.compile(r'(w|nw|ne|e|se|sw)')
    matches = directions.findall(path)
    coords = (0, 0)
    for match in matches:
        coords = tuple(a+b for a,b in zip(coords, ADJ[match]))
    return coords

counts = set()
for line in data:
    c = simplify(line)
    counts.remove(c) if c in counts else counts.add(c)

print(f'Part 1: {len(counts)}')

room = Room(counts)
room.cycle(100)
print(f'Part 2: {len(room.map)}')
