import time
with open("data.txt") as f:
    dat = f.read()

dat = [(x[:7], x[7:]) for x in dat.split('\n')[:-1]]

# Loops

start_time = time.time()
print("l o o p s")


def index(input_string, width, lower_char):
    s = 0
    e = width - 1
    current_width = width

    for c in input_string:
        if c == lower_char:
            e = e - (current_width)/2
            current_width /= 2
        else:
            s = s + (current_width)/2
            current_width /= 2
    # At this point s == e
    return int(s)


ids = [(8 * index(d[0], 128, 'F')) + index(d[1], 8, 'L') for d in dat]
ids.sort()

print("one: ", ids[-1])

for x, y in zip(ids[:], ids[1:]):
    if y-x == 2:
        print("two: ", int(x+1))
        break

print("Time: %f sec" % (time.time() - start_time))

# Converting to int directly
# Thanks r/adventofcode!
start_time = time.time()
print("Converting to an unsigned int directly")
print(dat[0][0])
print(dat[0][0].replace("B", "1").replace("F", "0"))

dat = [8*int(d[0].replace("B", "1").replace("F", "0"), 2) +
       int(d[1].replace("R", "1").replace("L", "0"), 2) for d in dat]
dat.sort()

print("one: ", dat[-1])
for x, y in zip(dat, dat[1:]):
    if y-x == 2:
        print("two: ", x+1)
        break

print("Time: %f sec" % (time.time() - start_time))
