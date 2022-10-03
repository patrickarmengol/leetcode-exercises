
def single_number(nums):
    d = {}
    for n in nums:
        if n in d:
            del d[n]
        else:
            d[n] = True
    return list(d.keys())[0]


def main():
    print(single_number([1, 2, 2, 1, 3, 3, 4, 5, 5]))

if __name__ == '__main__':
    main()


"""
Runtime: 292 ms, faster than 37.78% of Python3 online submissions for Single Number.
Memory Usage: 16.5 MB, less than 93.23% of Python3 online submissions for Single Number.

just went with my first thought of using a dictionary for limited mem usage
should have thought some more about other potential solutions

found this clever usage of xor in discussion:
def singleNumber(self, nums: List[int]) -> int:
	return reduce(lambda total, el: total ^ el, nums)
"""

