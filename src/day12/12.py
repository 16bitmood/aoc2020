import numpy as np
from math import sin, cos, radians
with open('data.txt') as f:
    dat = [(x[0], int(x[1:])) for x in f.read().split('\n') if x != '']


dirs = {
    'N': np.array([0.0, 1.0]),
    'S': np.array([0.0, -1.0]),
    'E': np.array([1.0, 0.0]),
    'W': np.array([-1.0, 0.0])
}


def manhattan_distance(vec):
    return round(abs(vec[0]) + abs(vec[1]))


def rotate(vec, degree):
    """
    |cos θ   −sin θ| |x| = |x cos θ − y sin θ| = |x'|
    |sin θ    cos θ| |y|   |x sin θ + y cos θ|   |y'|
    """
    theta = radians(degree)
    x = vec[0]*cos(theta) - vec[1]*sin(theta)
    y = vec[0]*sin(theta) + vec[1]*cos(theta)
    return np.array([x, y])


def one(insts):
    curr_loc = np.array([0.0, 0.0])
    curr_dir = np.array([1.0, 0.0])  # Starts at East
    for inst in insts:
        if inst[0] in 'NSEW':
            curr_loc += inst[1] * dirs[inst[0]]
        elif inst[0] == 'L':
            curr_dir = rotate(curr_dir, inst[1])
        elif inst[0] == 'R':
            curr_dir = rotate(curr_dir, -inst[1])
        elif inst[0] == 'F':
            curr_loc += inst[1] * curr_dir
        else:
            raise Exception('what')

    return manhattan_distance(curr_loc)


def two(insts):
    waypoint_loc = np.array([10.0, 1.0])  # Starting Waypoin Location
    distance_traveled = np.array([0.0, 0.0])
    for inst in insts:
        if inst[0] in 'NSEW':
            waypoint_loc += inst[1] * dirs[inst[0]]
        elif inst[0] == 'L':
            waypoint_loc = rotate(waypoint_loc, inst[1])
        elif inst[0] == 'R':
            waypoint_loc = rotate(waypoint_loc, -inst[1])
        elif inst[0] == 'F':
            distance_traveled += inst[1] * waypoint_loc
        else:
            raise Exception('what')

    return manhattan_distance(distance_traveled)


print('one: ', one(dat))
print('two: ', two(dat))
