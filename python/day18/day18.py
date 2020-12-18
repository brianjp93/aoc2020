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
        _line = line
        line = re.sub(r'(\d+\+\d+)', replace, line)
        line = re.sub(r'[\(\*](\d+\*\d+)[\)\*]', replace, line)
        line = re.sub(r'(\(\d+\))', lambda x: x.group(0)[1:-1], line)
        if '+' not in line or '*' not in line:
            return eval(line)

def replace(match_obj):
    part = match_obj.group(0)
    return part.replace(match_obj.group(1), str(eval(match_obj.group(1))))


total1 = sum(evaluate(''.join(line.strip().split())) for line in d)
total2 = sum(evaluate2(''.join(line.strip().split())) for line in d)
print(f'Part 1: {total1}')
print(f'Part 2: {total2}')
