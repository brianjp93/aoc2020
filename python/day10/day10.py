import pathlib
from collections import Counter

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    d = sorted([int(x.strip()) for x in f.read().strip().split('\n')])

d = [0] + d + [d[-1] + 3]
diffs = Counter(b-a for a, b in zip(d, d[1:]))

def c():
    cache = [1] + ([0] * (len(d)-1))
    for i in range(len(d)):
        for x in range(1, 4):
            if i >= x and d[i]-d[i-x] <= 3:
                cache[i] += cache[i-x]
    return cache[-1]

print(f'Part 1: {diffs[1] * diffs[3]}')
print(f'Part 2: {c()}')
