

def find_error_nums(nums):
    c = [0] * len(nums)
    for n in nums:
        c[n-1] += 1
    res = [-1, -1]
    for i, x in enumerate(c):
        if x == 0:
            res[1] = i + 1
        elif x == 2:
            res[0] = i + 1
    return res


def main():
    tests = [
        [1, 2, 2, 4],
        [1, 1]
    ]
    for test in tests:
        print(find_error_nums(test))

if __name__ == '__main__':
    main()


"""
of course there's a clever math solution

def find_error_nums(nums):
    n = len(nums)    
    s = n*(n+1)//2   # This code will calculate sum of 1-n numbers. please refer to Arithmetic Progression from Maths
    miss = s - sum(set(nums))  # set(num) will return unique elements from the list and the sum(set(nums)) will calculate the sum of unique elements from the list.
    duplicate = sum(nums) + miss - s # sum(nums) + miss no - sum of 1-n numbers will give us the duplicate
    return [duplicate, miss]

"""