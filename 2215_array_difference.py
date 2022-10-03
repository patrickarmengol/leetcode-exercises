def diff_two_arrays(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    return [list(s1.difference(s2)), list(s2.difference(s1))]


def main():
    print(diff_two_arrays([1, 2, 3], [2, 4, 6]))
    print(diff_two_arrays([1, 2, 3, 3], [1, 1, 2, 2]))

if __name__ == '__main__':
    main()


"""
Runtime: 466 ms, faster than 39.05% of Python3 online submissions for Find the Difference of Two Arrays.
Memory Usage: 14.4 MB, less than 15.82% of Python3 online submissions for Find the Difference of Two Arrays.

no idea why my solution is slow compared to others
all python answers in discussion are essentially the same
"""