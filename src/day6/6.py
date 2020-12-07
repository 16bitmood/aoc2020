with open("data.txt") as f:
    ans = [[set(x) for x in d.split('\n')]
           for d in f.read()[:-1].split('\n\n')]

print("one: ", sum(map(len, map(lambda x: set.union(*x), ans))))
print("two: ", sum(map(len, map(lambda x: set.intersection(*x), ans))))
