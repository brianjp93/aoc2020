import pathlib
import re
from itertools import permutations

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    d = [x.strip() for x in f.read().strip().split('\n')]


def apply_mask(n, mask):
    out = []
    nbin = f'{n:0b}'[::-1]
    for i, ch in enumerate(reversed(mask)):
        if ch != 'X':
            out.append(ch)
        elif i < len(nbin):
            out.append(nbin[i])
        else:
            out.append('0')
    out = out[::-1]
    out = ''.join(out)
    return int(out, 2)

def apply_mask2(n, mask):
    out = []
    nbin = f'{n:0b}'[::-1]
    revmask = mask[::-1]
    for i, ch in enumerate(revmask):
        if ch == '0' and i < len(nbin):
            out.append(nbin[i])
        else:
            out.append(ch)
    out = out[::-1]
    return ''.join(out)

def get_all_options(masked_num):
    all_options = []
    xcount = masked_num.count('X')
    for n in range(2**xcount):
        newoption = masked_num
        for i in f'{n:0b}'.zfill(xcount):
            newoption = newoption.replace('X', i, 1)
        all_options.append(int(newoption, 2))
    return all_options or [masked_num]


mem1 = {}
mem2 = {}
for line in d:
    if 'mask' in line:
        mask = line.split('=')[1].strip()
    elif 'mem' in line:
        addr, num = re.search(r'mem\[(\d+)\] = (\d+)', line).groups()
        addr, num = int(addr), int(num)
        masked_num = apply_mask(num, mask)
        masked_addr = apply_mask2(addr, mask)
        addresses = get_all_options(masked_addr)
        mem1[addr] = masked_num
        for addr in addresses:
            mem2[addr] = num

print(f'Part 1: {sum(mem1.values())}')
print(f'Part 2: {sum(mem2.values())}')
