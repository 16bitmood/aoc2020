with open("data.txt") as f:
    dat = f.read()

dat = dat.split('\n\n')
dat = [x.replace('\n', ' ').split() for x in dat]
passports = []

for x in dat:
    curr = {}
    for y in x:
        temp = y.split(':')
        curr[temp[0]] = temp[1]
    passports.append(curr)


def validate_height(h):
    return (h[-2:] == 'cm' and (150 <= int(h[:-2]) <= 193))\
        or (h[-2:] == 'in' and (59 <= int(h[:-2]) <= 76))


def check_two(p):
    try:
        return (1920 <= int(p['byr']) <= 2002) \
            and (2010 <= int(p['iyr']) <= 2020) \
            and (2020 <= int(p['eyr']) <= 2030) \
            and validate_height(p['hgt']) \
            and (len(p['hcl']) == 7 and int(p['hcl'][1:], 16)) \
            and (p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])\
            and (len(p['pid']) == 9 and int(p['pid']))
    except:
        return False


def check_one(p):
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    return required.issubset(set(p.keys()))


p1 = 0
p2 = 0

for p in passports:
    if check_one(p):
        p1 += 1
    if check_two(p):
        p2 += 1

print("one: ", p1)
print("two: ", p2)
