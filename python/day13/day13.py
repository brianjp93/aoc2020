import pathlib
import numpy as np
from sympy.ntheory.modular import solve_congruence

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    n, d = [x.strip() for x in f.read().strip().split('\n')]
    n = int(n)
    nums = {i: int(x) for i, x in enumerate(d.split(',')) if x != 'x'}


def get_wait(n, bus_id):
    return bus_id - (n % bus_id)


def find_start(nums):
    lcm = int(np.lcm.reduce(list(nums.values())))
    start, add_offset = 0, 1
    old_len = 0
    offset_dict = {}
    while True:
        for offset, bus in nums.items():
            group = [bus for offset, bus in nums.items() if (start+offset) % bus == 0]
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


first = min([(x, get_wait(n, x)) for x in nums.values()], key=lambda x: x[1])
print(f'Part 1: {first[0] * first[1]}')

start = find_start(nums)
print(f'Part 2: {start}')

# part 2 alternative method
# import solve_congruence from sympy lul
x = solve_congruence(*((x[1]-x[0], x[1]) for x in nums.items()))
print(x[0])
