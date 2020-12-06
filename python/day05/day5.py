import pathlib
import functools
import re

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')

def find_seat(word):
    word = re.sub(r'(B|R)', '1', re.sub(r'(F|L)', '0', word))
    return int(word[:7], 2), int(word[7:], 2)

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
