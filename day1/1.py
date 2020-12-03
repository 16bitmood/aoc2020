import time
# Data
with open('data.txt', 'r') as f:
    nums = f.read()

nums = [int(x) for x in nums.split("\n")[:-1]]

# Brute Force Solution
start_time = time.time()
print("Brute force")

ans1 = [x*y for x in nums for y in nums if x+y == 2020]
ans2 = [x*y*z for x in nums for y in nums for z in nums if x+y+z == 2020]

print("1:", ans1[0])
print("2:", ans2[0])

print("Time: %f sec" % (time.time() - start_time))

# Brute force only 1:
start_time = time.time()
print("Brute force exit on first solution")

found = False
for x in nums:
    for y in nums:
        if x+y == 2020:
            print("1: ", x*y)
            found = True
            break
    if found:
        break

found = False
for x in nums:
    for y in nums:
        for z in nums:
            if x+y+z == 2020:
                print("2: ", x*y*z)
                found = True
                break
        if found:
            break
    if found:
        break

print("Time: %f sec" % (time.time() - start_time))

# something else
print("Something else")
start_time = time.time()

nums.sort()

s = 0
e = len(nums)-1
required = 2020

while s < e:
    if nums[e] + nums[s] == required:
        print("1: ", nums[e]*nums[s])
        break
    if nums[e] + nums[s] < required:
        s += 1
    else:
        e -= 1

for c in range(len(nums)):
    s = 0
    e = len(nums)-1
    required = 2020 - nums[c]
    found = False
    while s < e:
        if nums[e] + nums[s] == required:
            print("1: ", nums[e]*nums[s]*nums[c])
            found = True
            break
        if nums[e] + nums[s] < required:
            s += 1
        else:
            e -= 1
    if found:
        break

print("Time: %f.5 sec" % (time.time() - start_time))
