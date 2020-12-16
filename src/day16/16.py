with open('data.txt') as f:
    dat = [[y for y in x.split('\n') if y != '']
           for x in f.read().split('\n\n') if x != '']

fields = dict()
for d in dat[0]:
    name, ranges = d.split(':')
    fields[name] = [[int(i) for i in v.strip().split('-')]
                    for v in ranges.split('or')]

my_ticket = [int(x) for x in dat[1][1].split(',') if x != '']

nearby_tickets = [[int(x) for x in y.split(',') if x != '']
                  for y in dat[2][1:]]


def error_rate(ticket):
    error_rate = 0
    for v in ticket:
        curr_is_valid = False
        for rs in fields.values():
            for r in rs:
                if (r[0] <= v <= r[1]):
                    # print(i, v, j)
                    curr_is_valid = True
                    break
            if curr_is_valid:
                break
        if not curr_is_valid:
            error_rate += v
    return error_rate


def possible_fields(v):
    possible = set()
    for f, rs in fields.items():
        for r in rs:
            if r[0] <= v <= r[1]:
                possible.add(f)
                break

    return possible


def two():
    valid_tickets = [t for t in nearby_tickets if error_rate(t) == 0]
    possible = [None] * len(nearby_tickets[0])
    for i in range(len(possible)):
        possible[i] = set.intersection(
            *(possible_fields(t[i]) for t in valid_tickets))
    while True:
        fixed = {list(f)[0] for i, f in enumerate(possible) if len(f) == 1}
        for i, p in enumerate(possible):
            if len(p) == 1:
                continue
            possible[i] -= fixed
        if len(fixed) == len(possible):
            possible = [list(possible[i])[0] for i in range(len(possible))]
            break

    prod = 1
    for i, p in enumerate(possible):
        if p.startswith('departure'):
            prod *= my_ticket[i]
    return prod


# print(fields)
print('one: ', sum(error_rate(t) for t in nearby_tickets))
print('two: ', two())
