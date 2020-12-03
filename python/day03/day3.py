import pathlib
import functools

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [line.strip() for line in f]

TREE = '#'
def count_trees_on_slope(data, dx, dy):
    max_x = len(data[0])
    max_y = len(data)
    x = y = count = 0
    while y < max_y:
        if data[y][x % max_x] == TREE:
            count += 1
        x += dx
        y += dy
    return count


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = [count_trees_on_slope(data, *x) for x in slopes]
print(f'Part 1: {counts[1]}')
print(f'Part 2: {functools.reduce(lambda x, y: x*y, counts)}')
