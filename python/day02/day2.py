import pathlib
import re

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    count1 = count2 = 0
    data = [x for x in f.readlines()]
    for x in data:
        low, high, letter, word = re.search(r'(\d+)-(\d+) (\w): (\w+)', x).groups()
        low = int(low)
        high = int(high)

        if low <= word.count(letter) <= high:
            count1 += 1

        if (word[low-1], word[high-1]).count(letter) == 1:
            count2 += 1


print(f'part 1: {count1}')
print(f'part 2: {count2}')
