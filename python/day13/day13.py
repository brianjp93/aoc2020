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
    start = 0
    add_offset = nums[0]
    offset_dict = {}
    while True:
        found = True
        for offset, bus in numsd.items():
            if (start + offset) % bus == 0:
                if bus in offset_dict:
                    diff = start - offset_dict[bus]
                    if diff > add_offset:
                        add_offset = diff
                offset_dict[bus] = start
            else:
                found = False
        if found:
            return start % lcm
        start += add_offset

start = find_start(numsd, nums)
print(f'Part 2: {start}')
