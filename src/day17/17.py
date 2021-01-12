from itertools import product
from copy import deepcopy as cp

with open('data.txt') as f:
    data = [[yx == '#' for yx in y] for y in f.read().split('\n') if y != ""]


class Space:
    # Not 'Optimal'? Yes
    # ~Functinoal~? Very
    def __init__(self, shape_rev, plane=None, offset=None):
        if shape_rev == []:
            self.space = False
        else:
            self.space = [Space(shape_rev[1:]) for _ in range(shape_rev[0])]
        self.shape = shape_rev

        if None not in (plane, offset):
            self.put_plane(plane, offset)

        self.a_s = set(
            product([0, +1, -1], repeat=self.dims())) - {(0,)*self.dims()}

    def dims(self):
        return len(self.shape)

    def __repr__(self):
        if self.dims() == 0:
            return '#' if self.space else '.'
        elif self.dims() == 1:
            return ''.join(s.__repr__() for s in self.space)
        elif self.dims() == 2:
            return f'{self.shape}\n'+'\n'.join(s.__repr__() for s in self.space)
        else:
            return "".join(f'\n{self.shape}{i}==================\n{s}'
                           for i, s in enumerate(self.space))

    def put(self, point, value):
        if point == []:
            self.space = value
        else:
            self.space[point[0]].put(point[1:], value)

    def get(self, point):
        if point == []:
            return self.space
        else:
            return self.space[point[0]].get(point[1:])

    def put_plane(self, plane, offset):
        x = [offset]*(self.dims() - 2)
        for j in range(len(plane)):
            for i in range(len(plane[0])):
                self.put(x + [offset + j, offset + i], plane[j][i])

    def active_around(self, point):
        # Just a hack
        return sum(self.get([(c1+c2) % m for c1, c2, m in zip(point, a, self.shape)])
                   for a in self.a_s)

    def total_active(self):
        if self.dims() == 0:
            return self.space
        else:
            return sum(s.total_active() for s in self.space)

    def points(self):
        return product(*map(range, self.shape))


def solve(shape, data, cycles):
    # Data => 8x8x1 , after 6 cycles => (8+6*2)x(8+6*2)x(1+6*2)
    space = Space([x + 2*cycles for x in shape], data, cycles)
    next_space = cp(space)
    for _ in range(cycles):
        for p in map(list, space.points()):
            k = space.active_around(p)
            if space.get(p) and k not in (2, 3):
                next_space.put(p, False)
            elif (not space.get(p)) and k == 3:
                next_space.put(p, True)

        space = cp(next_space)
        next_space = cp(next_space)

    return space.total_active()


def one():
    return solve([1, len(data), len(data[0])], data, 6)


def two():
    return solve([1, 1, len(data), len(data[0])], data, 6)


print("One", one())
print("two", two())
