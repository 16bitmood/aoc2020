from sympy.ntheory.modular import crt
from functools import reduce

with open('data.txt') as f:
    dat = [x for x in f.read().split('\n') if x != '']
    dat[0] = int(dat[0])
    dat[1] = [x for x in dat[1].split(',') if x != '']


def one(dat):
    leave_time = dat[0]
    busses = dat[1]
    valid_bus = None
    time_wait = 100000  # Or some other big number

    for b_id in busses:
        if b_id != 'x':
            b_id = int(b_id)
            x = b_id * (leave_time//b_id)
            if x < leave_time:
                x += b_id
            if x - leave_time < time_wait:
                valid_bus = b_id
                time_wait = x-leave_time

    return valid_bus * time_wait


# from reddit
def two(dat):
    a_s = []
    n_s = []

    for i, b_id in enumerate(dat[1]):
        if b_id != 'x':
            b_id = int(b_id)
            a_s.append(b_id)
            n_s.append(b_id - i)

    return crt(a_s, n_s)[0]


print('one: ', one(dat))
print('two: ', two(dat))
