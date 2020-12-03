import pathlib

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    nums = set(int(x.strip()) for x in f.readlines())

def find_group(nums, n, count):
    if n < 0:
        return None
    for i in nums:
        nums.remove(i)
        if count <= 2:
            if n-i in nums:
                return [i, n-i]
        else:
            possible = find_group(nums, n-i, count-1)
            if possible:
                return [i] + possible
        nums.add(i)

def prod(iterable):
    out = 1
    for i in iterable:
        out *= i
    return out

group = find_group(nums, 2020, 2)
print(f'Part 1: {prod(group)}')
group = find_group(nums, 2020, 3)
print(f'Part 2: {prod(group)}')
