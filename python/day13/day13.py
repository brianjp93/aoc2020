import pathlib
import numpy as np

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    n, d = [x.strip() for x in f.read().strip().split('\n')]
    n = int(n)
    d = d.split(',')
    nums = [int(x) for x in d if x != 'x']

def get_wait(n, bus_id):
    return bus_id - (n % bus_id)

first = min([(x, get_wait(n, x)) for x in nums], key=lambda x: x[1])
print(f'Part 1: {first[0] * first[1]}')

numsd = {i: int(x) for i, x in enumerate(d) if x != 'x'}

def find_start(numsd, nums):
    lcm = int(np.lcm.reduce(nums))
    start, add_offset = 0, 1
    old_len = 0
    offset_dict = {}
    while True:
        for offset, bus in numsd.items():
            group = [bus for offset, bus in numsd.items() if (start+offset) % bus == 0]
        if group:
            group.sort()
            group = tuple(group)
            if group in offset_dict:
                diff = start - offset_dict[group]
                if len(group) > old_len:
                    add_offset = diff
                    old_len = len(group)
            offset_dict[group] = start

        if len(group) == len(nums):
            return start % lcm
        start += add_offset

start = find_start(numsd, nums)
print(f'Part 2: {start}')
