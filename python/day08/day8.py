import pathlib
import re

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
                print(f'Instruction {self.index} already run. {self.data[self.index]}')
                print(f'acc: {self.acc}')
                break
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

    def reset(self):
        self.data = self._data[:]
        self.acc = 0
        self.index = 0
        self.index_history = set()

    def alter_test(self):
        swap = {'jmp': 'nop', 'nop': 'jmp'}
        for i, instr in enumerate(self._data):
            if 'jmp' in instr or 'nop' in instr:
                self.reset()
                datacopy = self._data[:]
                x = instr.split()[0]
                datacopy[i] = datacopy[i].replace(x, swap[x])
                self.data = datacopy

                for _ in range(1000):
                    try:
                        self.next()
                    except:
                        print(f'acc: {self.acc}')
                        break


comp = Comp(data)
comp.run()
comp.alter_test()