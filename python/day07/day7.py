import sys
import pathlib
import re
sys.path.append(str(pathlib.Path(__file__).absolute().parents[1]))

from helpers import memo

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [x.strip() for x in f.read().strip().split('\n')]

LEFT_REGEX = re.compile(r'(\w+ \w+) bags contain')
RIGHT_REGEX = re.compile(r'(\d+) (\w+ \w+)')
bags = {}
for line in data:
    bag = LEFT_REGEX.search(line).groups()[0]
    right = RIGHT_REGEX.findall(line)
    bags[bag] = {key: int(val) for val, key in right}

def has_bag(bagtype):
    count = 0
    for bag in bags:
        if check_bag(bag, bagtype):
            count += 1
    return count

@memo
def check_bag(bag, bagtype):
    out = False
    for inner in bags[bag]:
        if inner == bagtype:
            out = True
        elif check_bag(inner, bagtype):
            out = True
    return out

@memo
def _count_bags(bag):
    total = 1
    for inner, count in bags[bag].items():
        mult = _count_bags(inner)
        total += count * _count_bags(inner)
    return total
def count_bags(*args):
    return _count_bags(*args) - 1

print(f'Part 1: {has_bag("shiny gold")}')
print(f'Part 2: {count_bags("shiny gold")}')
