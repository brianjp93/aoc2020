import pathlib
import re
from string import ascii_lowercase
import copy

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    lines = [x.strip() for x in f.read().strip().split('\n')]
    rules = {}
    words = []
    for line in lines:
        line = line.strip()
        if line != '':
            if ':' in line:
                n, r = line.split(':')
                n = int(n)
                for part in r.split('|'):
                    part = part.strip().strip('"')
                    if part not in ascii_lowercase:
                        part = tuple(int(x) for x in part.split())
                    rules[n] = rules.get(n, []) + [part]
            else:
                words.append(line)


def get_rule(n, rules,  init=True):
    if isinstance(rules[n][0], str):
        return rules[n][0]
    out = []
    for part in rules[n]:
        temp = []
        for x in part:
            temp.append(f'({get_rule(x, rules, init=False)})')
        if temp:
            out.append(''.join(temp))
    if out:
        if init:
            return f'^{"|".join(out)}$'
        return '|'.join(out)
    return ''

rule = re.compile(get_rule(0, rules))
out = sum(rule.match(word) is not None for word in words)
print(f'Part 1: {out}')

rule_8 = get_rule(8, rules, init=False)
rule_11 = get_rule(11, rules, init=False)
rule_42 = get_rule(42, rules, init=False)
rule_31 = get_rule(31, rules, init=False)

total = 0
for i in range(5):
    rule_11_repeat = f'({rule_42}){{{i}}}{rule_11}({rule_31}){{{i}}}'
    rule = re.compile(f'^{rule_8}+{rule_11_repeat}$')
    for word in words:
        if rule.match(word):
            total += 1

print(f'Part 2: {total}')
