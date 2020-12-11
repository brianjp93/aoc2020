import pathlib
import functools

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [line.strip() for line in f]

TREE = '#'

def coords(dx, dy, max_x, max_y):
    coord = (0, 0)
    while coord[1] < max_y:
        yield coord
        coord = ((coord[0] + dx) % max_x, coord[1] + dy)

def count_trees_on_slope(data, dx, dy):
    return sum(data[y][x] == TREE for x, y in coords(dx, dy, len(data[0]), len(data)))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = [count_trees_on_slope(data, *x) for x in slopes]
print(f'Part 1: {counts[1]}')
print(f'Part 2: {functools.reduce(lambda x, y: x*y, counts)}')
