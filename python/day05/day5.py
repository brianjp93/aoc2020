import pathlib
import functools

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')

def find_seat(word):
    part1 = word[:7]
    part2 = word[7:]
    start = 1
    end = 128
    for ch in part1:
        size = end - start + 1
        if ch == 'F':
            end  -= size // 2
        elif ch == 'B':
            start += size // 2
    row = start - 1

    start = 1
    end = 8
    for ch in part2:
        size = end - start + 1
        if ch == 'L':
            end  -= size // 2
        elif ch == 'R':
            start += size // 2
    col = start - 1
    return row, col

def find_my_seat(seat_ids):
    seat_id_set = set(seat_ids)
    for x in seat_id_set:
        if x + 2 in seat_id_set and x + 1 not in seat_id_set:
            return x + 1


with open(filename) as f:
    data = [line.strip() for line in f]
    seat_ids = []
    for line in data:
        row, col = find_seat(line)
        seat_ids.append(row * 8 + col)

    print(f'Part 1: {max(seat_ids)}')
    print(f'Part 2: {find_my_seat(seat_ids)}')
