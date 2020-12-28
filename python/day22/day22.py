import pathlib
from collections import defaultdict

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    data = [x.strip() for x in f.read().strip().split('\n\n')]
    decks = [list(map(int, part.splitlines()[1:])) for part in data]
    p1, p2 = decks

def play(p1, p2):
    while p1 and p2:
        c1, c2 = p1.pop(0), p2.pop(0)
        if c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return p1, p2

def play2(p1, p2):
    history = set()
    while p1 and p2:
        state = tuple(p1), tuple(p2)
        if state in history:
            return 1, 0
        history.add(state)
        c1, c2 = p1.pop(0), p2.pop(0)
        winner = None
        if len(p1) >= c1 and len(p2) >= c2:
            a, b = play2(p1[:c1], p2[:c2])
            if a:
                winner = 1
        elif c1 > c2:
                winner = 1

        if winner:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return p1, p2

x, y = play(p1[:], p2[:])
winner = x or y
score = [n * (i+1) for i, n in enumerate(winner[::-1])]
print(f'Part 1: {sum(score)}')

x, y = play2(p1[:], p2[:])
winner = x or y
score = [n * (i+1) for i, n in enumerate(winner[::-1])]
print(f'Part 2: {sum(score)}')
