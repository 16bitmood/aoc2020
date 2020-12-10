with open('data.txt') as f:
    dat = [int(x) for x in f.read().split('\n') if x != '']
    dat.sort()
    dat = [0] + dat + [dat[-1]+3]


def one(arr):
    d = [0, 0, 0]
    for i in range(len(arr)-1):
        d[arr[i+1] - arr[i] - 1] += 1
    return d[0] * d[2]


def two(arr):
    from_point = [0] * len(arr)
    from_point[len(arr)-1] = 1
    for i in reversed(range(len(arr)-1)):
        for j in (1, 2, 3):
            if i+j < len(arr) and arr[i+j] - arr[i] <= 3:
                from_point[i] += from_point[i+j]
            else:
                break
    return from_point[0]


print("one: ", one(dat))
print("two: ", two(dat))

# Valid but super_slow
# def two(arr):
#     if len(arr) == 1:
#         return 1
#     return sum(two(arr[i:]) for i in range(1, min(len(arr), 4)) if arr[i] - arr[0] <= 3)
