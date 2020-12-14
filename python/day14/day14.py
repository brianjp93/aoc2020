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
    out = int(out, 2)
    return out

def apply_mask2(n, mask):
    out = []
    nbin = f'{n:0b}'[::-1]
    revmask = mask[::-1]
    for i, ch in enumerate(revmask):
        if ch in ['X', '1']:
            out.append(ch)
        elif ch == '0' and i < len(nbin):
            out.append(nbin[i])
        else:
            out.append('0')
    out = out[::-1]
    out = ''.join(out)
    return out

def get_all_options(masked_num):
    all_options = []
    xcount = masked_num.count('X')
    if xcount == 0:
        return [masked_num]
    rang = int('1'*xcount, 2) + 1
    for n in range(rang):
        newoption = masked_num
        for i in f'{n:0b}'.zfill(xcount):
            newoption = newoption.replace('X', i, 1)
        all_options.append(int(newoption, 2))
    return all_options


mem = {}
for line in d:
    if 'mask' in line:
        mask = line.split('=')[1].strip()
    elif 'mem' in line:
        addr, num = re.search(r'mem\[(\d+)\] = (\d+)', line).groups()
        addr, num = int(addr), int(num)
        masked_num = apply_mask(num, mask)
        mem[addr] = masked_num

print(sum(mem.values()))


mem = {}
for line in d:
    if 'mask' in line:
        mask = line.split('=')[1].strip()
    elif 'mem' in line:
        addr, num = re.search(r'mem\[(\d+)\] = (\d+)', line).groups()
        addr, num = int(addr), int(num)
        masked_addr = apply_mask2(addr, mask)
        addresses = get_all_options(masked_addr)
        for addr in addresses:
            mem[addr] = num

print(sum(mem.values()))
