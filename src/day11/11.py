import copy

with open('data.txt') as f:
    dat = [list(x) for x in f.read().split('\n') if x != '']


def check_one(i, j, dirs, m):
    count = 0
    cols, rows = len(m), len(m[0])
    for x, y in dirs:
        if 0 <= i+x < cols and 0 <= j+y < rows:
            if m[i+x][j+y] == '#':
                count += 1
    return count


def check_two(i, j, dirs, m):
    count = 0
    cols, rows = len(m), len(m[0])
    for x, y in dirs:
        for k in range(1, 10000):
            if 0 <= i+k*x < cols and 0 <= j+k*y < rows:
                if m[i+k*x][j+k*y] == '#':
                    count += 1
                    break
                elif m[i+k*x][j+k*y] == 'L':
                    break
            else:
                break
    return count


def iterate_mat(m, tol, check_func):

    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1),
            (-1, -1), (1, 1), (-1, 1), (1, -1)]

    prev = copy.deepcopy(m)
    cols, rows = len(m), len(m[0])

    while True:
        this = copy.deepcopy(prev)

        for i in range(cols):
            for j in range(rows):
                if prev[i][j] == 'L' and check_func(i, j, dirs, prev) == 0:
                    this[i][j] = '#'
                elif prev[i][j] == '#' and check_func(i, j, dirs, prev) >= tol:
                    this[i][j] = 'L'

        eq = True
        for i in range(cols):
            for j in range(rows):
                if this[i][j] != prev[i][j]:
                    eq = False
                    break
        if eq:
            return sum(1 for i in range(cols) for j in range(rows) if this[i][j] == '#')
        prev = this


print('one: ', iterate_mat(dat, 4, check_one))
print('two: ', iterate_mat(dat, 5, check_two))
