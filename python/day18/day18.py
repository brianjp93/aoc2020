import pathlib
import re

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    d = [x.strip() for x in f.read().strip().split('\n')]

def evaluate(line):
    while True:
        line = re.sub(r'(\(\d+\))', lambda x: x.group(0)[1:-1], line)
        line = re.sub(r'(\d+[\+\*]\d+)', replace, line, count=1)
        if line.isdigit():
            return int(line)



def evaluate2(line):
    while True:
        while True:
            _line = line
            line = re.sub(r'(\d+\+\d+)', replace, line)
            if line == _line:
                break
        while True:
            _line = line
            line = re.sub(r'[\(\*](\d+\*\d+)[\)\*]', replace, line)
            if line == _line:
                break
        line = re.sub(r'(\(\d+\))', lambda x: x.group(0)[1:-1], line)
        if '+' not in line or '*' not in line:
            return eval(line)
    return line

def replace(match_obj):
    part = match_obj.group(0)
    return part.replace(match_obj.group(1), str(eval(match_obj.group(1))))


total = 0
total2 = 0
for line in d:
    line = ''.join(line.strip().split())
    out = evaluate(line)
    out2 = evaluate2(line)
    total += out
    total2 += out2
print(f'Part 1: {total}')
print(f'Part 2: {total2}')
