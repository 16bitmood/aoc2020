with open("data.txt") as f:
    dat = f.read().split('\n')[:-1]

# Surprisingly, this horrible 'parser' works
dat = [x.split('contain') for x in dat]
dat = [(x.strip().rsplit(' ', 1)[0], [z.rsplit(' ', 1)[0].split(maxsplit=1)
                                      for z in y.strip().split(',')]) for x, y in dat]

rules = {}

for k, v in dat:
    rules[k] = [x for x in v if x[0] != 'no']


def check_bag(bag, to_check):
    for num, b in rules[bag]:
        if b == to_check:
            return True
        else:
            if check_bag(b, to_check):
                return True
    return False


def get_number(bag):
    if rules[bag] == []:
        return 0
    return sum(int(n) * (get_number(b) + 1) for n, b in rules[bag])


print("one ", sum(check_bag(b, 'shiny gold') for b in rules.keys()))
print("two ", get_number('shiny gold'))
