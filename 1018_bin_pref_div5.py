def prefix_div_by_5(nums):
    binary_string = ''.join(str(b) for b in nums)
    return [int(binary_string[:i+1], 2) % 5 == 0 for i in range(len(binary_string))]

def better_prefix_div_by_5(nums):
    r = []
    n = 0
    for b in nums:
        n = (n << 1) | b
        r.append(n % 5 == 0)
    return r

def even_better_prefix_div_by_5(nums):
    r = []
    n = 0
    for b in nums:
        n = ((n << 1) | b) % 5 # reset so that n doesn't grow
        r.append(n == 0)
    return r

def concise_prefix_div_by_5(nums):
    return [x % 5 == 0 for x in accumulate(nums, lambda x, y: (x << 1) + y)]


def main():
    print(prefix_div_by_5([0, 1, 1]))
    print(prefix_div_by_5([1, 1, 1]))

if __name__ == '__main__':
    main()


"""
Runtime: 2039 ms, faster than 5.05% of Python3 online submissions for Binary Prefix Divisible By 5.
Memory Usage: 16.5 MB, less than 9.66% of Python3 online submissions for Binary Prefix Divisible By 5.

holy heck, my original solution is bad
"""
