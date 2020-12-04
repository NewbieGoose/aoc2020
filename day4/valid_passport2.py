#!/usr/bin/env python3

import sys
import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']

required_fields_val = {
    'byr' : lambda x: len(x) == 4 and (1920 <= int(x) <= 2002),
    'iyr' : lambda x: len(x) == 4 and (2010 <= int(x) <= 2020),
    'eyr' : lambda x: len(x) == 4 and (2020 <= int(x) <= 2030),
    'hgt' : lambda x: (x.endswith('cm') and 150 <= int(x[:-2]) <= 193)
                        or (x.endswith('in') and 59 <= int(x[:-2]) <= 76),
    'hcl' : lambda x: re.match(r'^#[a-f0-9]{6}$', x),
    'ecl' : lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid' : lambda x: re.match(r'^[0-9]{9}$',x)
}

def make_pass(passp):
    passport = {}
    for line in passp:
        for field in line.split():
            key, value = field.split(':',2)
            passport[key] = value
    return passport

def is_valid_pass(passport):
    def apply_validation(key):
        return required_fields_val[key](passport[key]) if key in passport else False
    validator = [apply_validation(key) for key in required_fields]
    return all(validator)

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]

    passports = []
    with open(FILENAME) as fd:
        temp_passport = []
        for line in fd:
            line  = line.strip()
            if not line:
                passport = make_pass(temp_passport)
                temp_passport = []
                if passport:
                    passports.append(passport)
            else:
                temp_passport.append(line)
        if temp_passport:
            passport = make_pass(temp_passport)
            if passport:
                passports.append(passport)
    valid_passports = [passport for passport in passports if is_valid_pass(passport)]
    print(f'Valid passports: {len(valid_passports)} out of the {len(passports)}')
