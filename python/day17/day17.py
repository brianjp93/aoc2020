from collections import defaultdict
from itertools import product

d = """
#.##....
.#.#.##.
###.....
....##.#
#....###
.#.#.#..
.##...##
#..#.###
""".strip().splitlines()
ACTIVE = '#'


class Space:
    def __init__(self, d, dim=3):
        self.dim = dim
        self.origin = (0,) * dim
        self.process(d)
        self.near_count = None

    def process(self, d):
        self.active = set()
        for y, row in enumerate(d):
            for x, ch in enumerate(row):
                if ch == ACTIVE:
                    self.active.add((x, y) + ((0,) * (self.dim - 2)))

    def near(self, coords):
        for p in product((1, 0, -1), repeat=self.dim):
            if p != self.origin:
                yield tuple(a+b for a,b in zip(coords, p))

    def count_near(self):
        self.near_count = defaultdict(int)
        for coord in self.active:
            for other in self.near(coord):
                self.near_count[other] += 1

    def next(self):
        self.count_near()
        active = set()
        for coord, count in self.near_count.items():
            if count == 3:
                active.add(coord)
            elif count == 2 and coord in self.active:
                active.add(coord)
        self.active = active


for i in range(2):
    s = Space(d, dim=3+i)
    for _ in range(6):
        s.next()
    print(f'Part {i+1}: {len(s.active)}')
