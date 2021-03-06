import time
import re

# Simple Parsing using builtin functions
start_time = time.time()

with open("data.txt") as f:
    dat = f.read()

dat = [x.split(' ') for x in dat.split('\n')[:-1]]

# Parsing "1-3 b: bebasdfea" => "[1, 3, 'b', "bebasdfea"]"
dat = [(*[int(y) for y in x[0].split('-')], x[1][0], x[2]) for x in dat]


def check_part_one(first, second, char, password):
    return first <= password.count(char) <= second


def check_part_two(first, second, char, password):
    return (password[first - 1] == char) ^ (password[second - 1] == char)


print("one:", len(list(filter(lambda x: check_part_one(*x), dat))))
print("two:", len(list(filter(lambda x: check_part_two(*x), dat))))

print("Time: %f sec" % (time.time() - start_time))

# Parsing using Regular Expression

start_time = time.time()

with open("data.txt") as f:
    dat = f.read()

p = re.compile("(\d+)-(\d+) ([a-z]): ([a-z]+)")
c1 = 0
c2 = 0

for m in re.findall(p, dat):
    if int(m[0]) <= m[3].count(m[2]) <= int(m[1]):
        c1 += 1
    if (m[3][int(m[0])-1] == m[2]) ^ (m[3][int(m[1])-1] == m[2]):
        c2 += 1

print("one:", c1)
print("two:", c2)
print("Time: %f sec" % (time.time() - start_time))
