with open("data.txt") as f:
    dat = f.read()

dat = dat.split('\n')[:-1]
width = len(dat[0])

trees = []

for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    x = 0
    y = 0
    curr = 0
    while y + d < len(dat):
        x = (x+r) % width
        y += d
        if dat[y][x] == '#':
            curr += 1

    trees.append(curr)

p = 1
for x in trees:
    p *= x

print("one: ", trees[1])
print("two: ", p)
