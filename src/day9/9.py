with open('data.txt') as f:
    dat = [int(x) for x in f.read().split('\n')[:-1]]


def check_sum(required, nums):
    # Reusing day1 as a function
    nums.sort()
    s = 0
    e = len(nums)-1
    while s < e:
        if nums[e] + nums[s] == required:
            return True
        if nums[e] + nums[s] < required:
            s += 1
        else:
            e -= 1
    return False


def find_two(invalid, nums):
    for i in range(len(nums)):
        s = i
        e = 1+i
        while True:
            to_check = sum(nums[s:e+1])
            if to_check == invalid:
                return min(nums[s:e+1]) + max(nums[s:e+1])
            if to_check > invalid:
                break
            else:
                e += 1


for i in range(len(dat)):
    preamble = dat[i:25+i]
    if not check_sum(dat[25+i], preamble):
        one = dat[25+i]
        print("one :", one)
        print("two :", find_two(one, dat))
        break
