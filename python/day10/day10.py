import pathlib
from functools import lru_cache
from collections import Counter

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    d = sorted([int(x.strip()) for x in f.read().strip().split('\n')])

d = [0] + d + [d[-1] + 3]
diffs = Counter(b-a for a, b in zip(d, d[1:]))

@lru_cache(None)
def c(i=0):
    if i == len(d) - 1:
        return 1
    return sum(c(i+x) for x in range(1, 4) if i+x < len(d) and d[i+x]-d[i] <= 3)

print(f'Part 1: {diffs[1] * diffs[3]}')
print(f'Part 2: {c()}')
