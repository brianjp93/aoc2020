import pathlib

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    d = [x.strip() for x in f.read().strip().split('\n')]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, int):
            return Point(self.x + other, self.y + other)
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        return Point(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False

    def rot_90(self, n):
        for i in range(n):
            self.x, self.y = -self.y, self.x

    def manhattan(self, other=None):
        if other is None:
            return abs(self.x) + abs(self.y)
        else:
            return abs(self.x - other.y) + abs(self.y - other.y)


CARDINAL = {
    'N': Point(0, -1),
    'E': Point(1, 0),
    'S': Point(0, 1),
    'W': Point(-1, 0),
}
DIRS = list(CARDINAL.values())


def do_move(d, pos, facing):
    for move in d:
        instr, dist = move[0], int(move[1:])
        if instr in CARDINAL:
            pos = pos + (CARDINAL[instr] * dist)
        elif instr == 'F':
            pos = pos + (facing * dist)
        else:
            change = int((1 if instr == 'R' else 3) * dist) // 90
            facing = DIRS[(DIRS.index(facing) + change) % len(DIRS)]
            newmove = Point(0, 0)
    return pos


def do_move2(d, pos, waypoint):
    for move in d:
        instr, dist = move[0], int(move[1:])
        if instr in CARDINAL:
            waypoint = waypoint + (CARDINAL[instr] * dist)
        elif instr == 'F':
            pos = pos + (waypoint * dist)
        else:
            change = 1 if instr == 'R' else 3
            change = int(change * dist) // 90
            waypoint.rot_90(change)
    return pos


pos = do_move(d, Point(0, 0), Point(1, 0))
print(pos.manhattan())

pos = do_move2(d, Point(0, 0), Point(10, -1))
print(pos.manhattan())
