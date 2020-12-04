import pathlib
import re

CWD = pathlib.Path(__file__).parent.absolute()
filename = pathlib.PurePath(CWD, 'data')


class Passport:
    def __init__(self, data):
        self.fields = self.process(data)

    def process(self, data):
        out = {}
        for row in data.splitlines():
            for item in row.split():
                key, val = item.split(':')
                out[key] = val
        return out

    def is_valid(self):
        return len(self.fields) == 8 or (len(self.fields) == 7 and self.fields.get('cid', None) is None)

    def is_valid2(self):
        return all([
            self.is_valid(),
            self.validate_date('byr', 1920, 2002),
            self.validate_date('iyr', 2010, 2020),
            self.validate_date('eyr', 2020, 2030),
            self.validate_hgt(),
            self.validate_hcl(),
            self.fields.get('ecl', None) in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            re.match('^[0-9]{9}$', self.fields.get('pid', '')),
        ])

    def validate_date(self, key, start, end):
        return start <= int(self.fields.get(key, 0)) <= end

    def validate_hgt(self):
        hgt = self.fields.get('hgt', '')
        if hgt.endswith('cm'):
            hgtnum = int(hgt[:-2])
            return 150 <= hgtnum <= 193
        elif hgt.endswith('in'):
            hgtnum = int(hgt[:-2])
            return 59 <= hgtnum <= 76
        return False

    def validate_hcl(self):
        hcl = self.fields.get('hcl', '')
        return hcl.startswith('#') and re.match(r'^[a-f0-9]{6}$', hcl[1:])


with open(filename) as f:
    data = f.read()
    all_passports = [Passport(group) for group in data.strip().split('\n\n')]

    valid_count = sum(x.is_valid() for x in all_passports)
    print(f'Part 1: {valid_count}')
    valid_count = sum(x.is_valid2() for x in all_passports)
    print(f'Part 2: {valid_count}')
