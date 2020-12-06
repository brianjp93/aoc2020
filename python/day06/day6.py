import pathlib
import re

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [x.strip() for x in f.read().split('\n\n')]

inters = []
unions = []
for group in data:
    people = group.splitlines()
    groupsets = []
    for person in people:
        groupsets.append(set(ch for ch in person))
    inter = groupsets[0].intersection(*groupsets)
    union = groupsets[0].union(*groupsets)
    inters.append(inter)
    unions.append(union)

print(f'Part 1: {sum(len(x) for x in unions)}')
print(f'Part 2: {sum(len(x) for x in inters)}')
