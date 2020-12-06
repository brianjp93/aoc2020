import pathlib
import re

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [x.strip() for x in f.read().split('\n\n')]

inters = []
unions = []
for group in data:
    groupsets = [set(ch for ch in person) for person in group.splitlines()]
    inters.append(groupsets[0].intersection(*groupsets))
    unions.append(groupsets[0].union(*groupsets))

print(f'Part 1: {sum(len(x) for x in unions)}')
print(f'Part 2: {sum(len(x) for x in inters)}')
