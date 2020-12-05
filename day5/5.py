with open("data.txt") as f:
    dat = f.read()

dat = [(x[:7], x[7:]) for x in dat.split('\n')[:-1]]


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
    # At the point s == e
    return int(s)


ids = [(8 * index(d[0], 128, 'F')) + index(d[1], 8, 'L') for d in dat]
ids.sort()

print("one: ", ids[-1])

for x, y in zip(ids[:], ids[1:]):
    if y-x == 2:
        print("two: ", int((x+y)/2))
        break
