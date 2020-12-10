import pathlib
from collections import deque

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [int(x.strip()) for x in f.read().strip().split('\n')]

preamble = 25
nset = set()
q = deque()

start, end = 0, 1
cursum = None

for i, n in enumerate(data):
    if len(q) >= preamble:
        found = False
        for check in q:
            if n - check in nset:
                found = True
                break
        if not found:
            invalid = n
            break
    q.append(n)
    nset.add(n)
    if len(q) > preamble:
        popnum = q.popleft()
        if popnum in nset:
            nset.remove(popnum)

while True:
    if cursum is None:
        cursum = sum(data[start:end])

    if cursum < invalid:
        end += 1
        cursum += data[end-1]
    elif cursum > invalid:
        start += 1
        end = start + 1
        cursum = None
    else:
        minmax = min(data[start:end]) + max(data[start:end])
        break

print(invalid)
print(minmax)
