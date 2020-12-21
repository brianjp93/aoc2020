import pathlib
import re
from string import ascii_lowercase

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'test')
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


def get_rule(n):
    if isinstance(rules[n][0], str):
        return [rules[n][0]]
    out = []
    for group in rules[n]:
        part = []
        for x in group:
            part = part + get_rule(x)
        out.append(part)
    return out

print(get_rule(0))
# print(words)
# print(rules)
