import pathlib
import re

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [int(x.strip()) for x in f.read().strip().split('\n')]


class IterableSum:
    def __init__(self, data, n=25, count=25):
        self.data = data[:]
        self.i = 0
        self.n = n
        self.count = count
        self.nums = {}
        self.invalid_num = None

    def start(self):
        for num in self.data[self.i: self.i+self.n]:
            self.nums[num] = self.nums.get(num, 0) + 1
        self.i = self.n

    def add(self, n):
        self.nums[n] = self.nums.get(n, 0) + 1

    def remove(self, n):
        self.nums[n] = self.nums[n] - 1
        if self.nums[n] == 0:
            del self.nums[n]

    def run(self):
        self.start()
        while True:
            output = self.next()
            if output == 'invalid':
                break

    def check(self):
        for sub in self.data[self.i-self.count: self.i]:
            self.remove(sub)
            if self.data[self.i] - sub in self.nums:
                self.add(sub)
                return True
            self.add(sub)

    def next(self):
        if self.check():
            self.remove(self.data[self.i-self.count])
            self.add(self.data[self.i])
            self.i += 1
            return 'valid'
        self.invalid_num = self.data[self.i]
        return 'invalid'

    def find_contig(self, findnum):
        start = 0
        end = 1
        cursum = None
        while True:
            if cursum is None:
                cursum = sum(self.data[start:end])

            if cursum < findnum:
                end += 1
                cursum += self.data[end-1]
            elif cursum > findnum:
                start += 1
                end = start + 1
                cursum = None
            else:
                return min(self.data[start:end]) + max(self.data[start:end])

itersum = IterableSum(data, n=25, count=25)
itersum.run()
print(f'Part 1: {itersum.invalid_num}')
print(f'Part 2: {itersum.find_contig(itersum.invalid_num)}')
