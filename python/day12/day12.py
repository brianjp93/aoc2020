import pathlib

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    d = [x.strip() for x in f.read().strip().split('\n')]

CARDINAL = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}

DIRS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]


def do_move(move, pos, facing):
    instr = move[0]
    dist = int(move[1:])
    if instr in CARDINAL:
        newmove = (CARDINAL[instr][0] * dist, CARDINAL[instr][1] * dist)
        pos = tuple(a+b for a,b in zip(pos, newmove))
    elif instr == 'F':
        newmove = (facing[0]*dist, facing[1]*dist)
        pos = tuple(a+b for a,b in zip(pos, newmove))
    else:
        change = 1 if instr == 'R' else -1
        change = int(change * dist) // 90
        facing = DIRS[(DIRS.index(facing) + change) % len(DIRS)]
        newmove = (0, 0)
    return pos, facing


def do_move2(move, pos, waypoint):
    instr = move[0]
    dist = int(move[1:])
    if instr in CARDINAL:
        newmove = (CARDINAL[instr][0] * dist, CARDINAL[instr][1] * dist)
        waypoint = tuple(a+b for a,b in zip(waypoint, newmove))
    elif instr == 'F':
        newmove = (waypoint[0]*dist, waypoint[1]*dist)
        pos = tuple(a+b for a,b in zip(pos, newmove))
    else:
        change = 1 if instr == 'R' else 3
        change = int(change * dist) // 90
        for i in range(change):
            waypoint = (-waypoint[1], waypoint[0])
    return pos, waypoint


pos = (0, 0)
facing = (1, 0)
for move in d:
    pos, facing = do_move(move, pos, facing)
print(sum(map(abs, pos)))

pos = (0, 0)
waypoint = (10, -1)
for move in d:
    pos, waypoint = do_move2(move, pos, waypoint)
print(sum(map(abs, pos)))
