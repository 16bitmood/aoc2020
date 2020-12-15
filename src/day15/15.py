start = [2, 0, 1, 9, 5, 19]


def solve(index):
    seq = [None]*index
    seq[:len(start)] = start
    spoken_at = {}

    for i in range(len(start)):
        spoken_at[seq[i]] = [i]

    step = 0
    for i in range(len(start), index):
        indexes = spoken_at.get(seq[i-1])
        if len(indexes) == 1:
            seq[i] = 0
            spoken_at[0].append(i)
        else:
            p, q = indexes[-2:]
            seq[i] = q-p
            if not spoken_at.get(q-p):
                spoken_at[q-p] = [i]
            else:
                spoken_at[q-p].append(i)
    return seq[-1]


print('one: ', solve(2020))
print('two: ', solve(30000000))
