import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [line.strip() for line in f]


EMPTY = '.'
TREE = '#'


class Forest:
    def __init__(self, data):
        self.max_x = self.max_y = 0
        self.map = self.process(data)

    def process(self, data):
        out = {}
        for y, row in enumerate(data):
            self.max_y = max(self.max_y, y)
            for x, ch in enumerate(row):
                self.max_x = max(self.max_x, x)
                out[(x, y)] = ch
        return out

    def count_trees_on_slope(self, dx, dy):
        x = y = count = 0
        while y <= self.max_y:
            if self.get(x, y) == TREE:
                count += 1
            x += dx
            y += dy
        return count

    def get(self, x, y):
        return self.map[(x % (self.max_x+1), y)]

def prod(iterable):
    out = 1
    for i in iterable:
        out *= i
    return out


forest = Forest(data)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = [forest.count_trees_on_slope(*x) for x in slopes]
print(prod(counts))
