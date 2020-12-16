import pathlib
from functools import reduce

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    d = [x.strip() for x in f.read().strip().split('\n\n')]

class Field:
    def __init__(self, name, ranges=None):
        self.name = name
        self.ranges = ranges or []

    def is_valid(self, n):
        return any(n in x for x in self.ranges)

class AllFields:
    def __init__(self):
        self.fields = []

    def matches_any(self, x):
        return any(field.is_valid(x) for field in self.fields)


def parse(data):
    af = AllFields()
    for line in data[0].splitlines():
        place, pos = line.strip().split(':')
        pos = pos.split(' or ')
        field = Field(place.strip())
        af.fields.append(field)
        for x in pos:
            a, b = [int(n) for n in x.split('-')]
            field.ranges.append(range(a, b+1))
    mine = [int(x) for x in data[1].splitlines()[1].split(',')]
    tickets = []
    for row in data[2].splitlines()[1:]:
        tickets.append([int(x) for x in row.split(',')])
    return af, mine, tickets

def get_mapping(af, valid_tickets):
    valid = {}
    columns = {}
    for row in valid_tickets:
        for i, num in enumerate(row):
            columns[i] = columns.get(i, set()) | {num}
    for col, nums in columns.items():
        for field in af.fields:
            inter = [x for x in nums if field.is_valid(x)]
            if len(inter) >= len(nums):
                valid[col] = valid.get(col, set()) | {field.name}
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
            return {key: value.pop() for key, value in valid.items()}

def remove_invalid(af, tickets):
    invalid = []
    valid_tickets = []
    for row in tickets:
        is_valid = True
        for num in row:
            if not af.matches_any(num):
                invalid.append(num)
                is_valid = False
        if is_valid:
            valid_tickets.append(row)
    return invalid, valid_tickets

af, mine, tickets = parse(d)
invalid, valid_tickets = remove_invalid(af, tickets)
print(sum(invalid))

mapping = get_mapping(af, valid_tickets)
out = [mine[key] for key, val in mapping.items() if val.startswith('departure')]
print(reduce(lambda x, y: x*y, out))
