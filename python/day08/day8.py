import pathlib
import re
import time

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')
with open(filename) as f:
    data = [x.strip() for x in f.read().strip().split('\n')]


class Comp:
    def __init__(self, data):
        self._data = data[:]
        self.data = data[:]
        self.acc = 0
        self.index = 0
        self.index_history = set()
        self.ACTIONS = {
            'nop': self.do_nop,
            'acc': self.do_acc,
            'jmp': self.do_jmp,
        }

    def run(self):
        while True:
            if self.index in self.index_history:
                return 'loop'
            elif self.index == len(self.data):
                return 'exit'
            self.index_history.add(self.index)
            self.next()

    def next(self):
        instr, num = self.data[self.index].split()
        num = int(num)
        self.ACTIONS[instr](num)

    def do_acc(self, arg):
        self.acc += arg
        self.index += 1

    def do_nop(self, arg):
        self.index += 1

    def do_jmp(self, arg):
        self.index += arg

    def reset(self, reset_data=True):
        if reset_data:
            self.data = self._data[:]
        self.acc = 0
        self.index = 0
        self.index_history = set()

    def alter_test(self):
        swap = {'jmp': 'nop', 'nop': 'jmp'}
        self.reset(reset_data=False)
        for i, instr in enumerate(self._data):
            if 'jmp' in instr or 'nop' in instr:
                self.reset(reset_data=False)
                x = instr.split()[0]
                self.data[i] = instr.replace(x, swap[x])
                exit_code = self.run()
                self.data[i] = instr
                if exit_code != 'loop':
                    break


comp = Comp(data)
comp.run()
print(f'Part 1: {comp.acc}')
comp.alter_test()
print(f'Part 2: {comp.acc}')
