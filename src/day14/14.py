import re
with open('data.txt') as f:
    dat = [x for x in f.read().split('\n') if x != '']

pat = re.compile('(mask = ([0|1|X]+)|mem\[(\d+)\] = (\d+))')


def one_mask(mk, val):
    mk_1 = int(mk.replace('X', '0'), 2)
    mk_2 = int(mk.replace('X', '1'), 2)
    return (val | mk_1) & mk_2


def two_masks(mask, val):
    def check(m, v):
        if m == '0':
            return v
        elif m == '1':
            return '1'
        else:
            return 'X'

    def iter_x(x):
        if x.count('X') == 0:
            return [int(x, 2)]
        return iter_x(x.replace('X', '0', 1)) +\
            iter_x(x.replace('X', '1', 1))

    to_make = ''.join(check(m, v) for m, v in zip(mask, f'{val:036b}'))
    return iter_x(to_make)


def solve(insts, part):
    mem = {}
    curr_mask = None

    for x in insts:
        _, mask, mem_addr, mem_val = pat.findall(x)[0]

        if mask != '':
            curr_mask = mask
        else:
            mem_val = int(mem_val)
            mem_addr = int(mem_addr)
            if part == 'one':
                mem[mem_addr] = one_mask(curr_mask, mem_val)
            else:
                for mk in two_masks(curr_mask, mem_addr):
                    mem[mk] = mem_val

    s = sum(v for v in mem.values())
    return s


print('one: ', solve(dat, 'one'))
print('two: ', solve(dat, 'two'))
