import pathlib
import re

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [x.strip() for x in f.read().strip().split('\n')]


bags = {}
for line in data:
    bag, others = line.split('bags contain')
    bag = bag.strip()
    bags[bag] = {}
    others = others.strip()
    for otherbag in others.split(','):
        otherbag = otherbag.strip().strip('bags.').strip('bag.').strip()
        if 'no other' not in otherbag:
            bagsplit = otherbag.split(' ')
            num = bagsplit[0]
            bagtype = bagsplit[1:]
            bagtype = ' '.join(bagtype)
            bags[bag][bagtype] = int(num)

cache = {}
count_inner = {}
def has_bag(bagtype):
    count = 0
    for bag, innerbags in bags.items():
        if check_bag(bag, bagtype):
            count += 1
    return count

def check_bag(bag, bagtype):
    for inner in bags[bag]:
        if inner == bagtype:
            cache[bag] = True
            return True
        if cache.get(inner) is True:
            cache[bag] = True
            return True
        elif cache.get(inner) is False:
            continue
        elif check_bag(inner, bagtype):
            cache[bag] = True
            return True
    cache[bag] = False
    return False

def count_bags(bag):
    if len(bags[bag]) == 0:
        return 1
    else:
        total = 1
        for inner, count in bags[bag].items():
            if inner in count_inner:
                total += (count * count_inner[inner])
            else:
                total += (count * count_bags(inner))
        count_inner[bag] = total
        return total


count = has_bag('shiny gold')
print(count)

print(count_bags('shiny gold') - 1)
