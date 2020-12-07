import pathlib
import re
from functools import lru_cache

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

@lru_cache
def check_bag(bag, bagtype):
    for inner in bags[bag]:
        if inner == bagtype or check_bag(inner, bagtype):
            return True
    return False

@lru_cache
def count_bags(bag, start=0):
    for inner, count in bags[bag].items():
        start += count * count_bags(inner, start=1)
    return start

print(f'Part 1: {has_bag("shiny gold")}')
print(f'Part 2: {count_bags("shiny gold")}')
