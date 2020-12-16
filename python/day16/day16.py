import pathlib
from functools import reduce

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    d = [x.strip() for x in f.read().strip().split('\n\n')]

def parse(data):
    locs = {}
    for line in data[0].splitlines():
        place, pos = line.strip().split(':')
        pos = pos.split(' or ')
        locs[place.strip()] = set()
        for x in pos:
            a, b = [int(n) for n in x.split('-')]
            locs[place.strip()] |= set(range(a, b+1))

    mine = [int(x) for x in data[1].splitlines()[1].split(',')]

    tickets = []
    for row in data[2].splitlines()[1:]:
        tickets.append([int(x) for x in row.split(',')])

    return locs, mine, tickets

def get_valid(locs, valid_tickets):
    valid = {}
    tickets = {}
    for row in valid_tickets:
        for i, num in enumerate(row):
            tickets[i] = tickets.get(i, set()) | {num}

    for col, nums in tickets.items():
        for name, possible in locs.items():
            inter = possible.intersection(nums)
            if len(inter) >= len(nums):
                valid[col] = valid.get(col, set()) | {name}

    while True:
        all_found = True
        for col, names in valid.items():
            if len(names) == 1:
                for other in valid:
                    if other != col:
                        valid[other] = valid[other] - names
            else:
                all_found = False

        if all_found:
            break
    return {key: value.pop() for key, value in valid.items()}

def get_invalid(locs, tickets):
    all_valid = set.union(*locs.values())
    invalid = []
    valid_tickets = []
    for row in tickets:
        is_valid = True
        for num in row:
            if num not in all_valid:
                invalid.append(num)
                is_valid = False
        if is_valid:
            valid_tickets.append(row)
    return invalid, valid_tickets

locs, mine, tickets = parse(d)

invalid, valid_tickets = get_invalid(locs, tickets)
print(sum(invalid))

mapping = get_valid(locs, valid_tickets)
out = [mine[key] for key, val in mapping.items() if val.startswith('departure')]
print(reduce(lambda x, y: x*y, out))
