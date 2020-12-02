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
