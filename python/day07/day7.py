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

@lru_cache(None)
def check_bag(bag, bagtype):
    for inner in bags[bag]:
        if inner == bagtype or check_bag(inner, bagtype):
            return True
    return False

@lru_cache(None)
def count_bags(bag, start=0):
    for inner, count in bags[bag].items():
        start += count * count_bags(inner, start=1)
    return start

print(f'Part 1: {sum(check_bag(bag, "shiny gold") for bag in bags)}')
print(f'Part 2: {count_bags("shiny gold")}')
