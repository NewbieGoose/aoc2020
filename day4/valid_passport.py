#!/usr/bin/env python3

import sys

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']

def make_pass(passp):
    passport = {}
    for line in passp:
        for field in line.split():
            key, value = field.split(':',2)
            passport[key] = value
    return passport

def is_valid_pass(passport):
    validator = [passport.get(key, False) for key in required_fields]
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
