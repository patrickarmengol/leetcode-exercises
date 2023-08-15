"""
neetcode - binary search - 1

sol:
just modify python's built-in bisect_left()
adding a check for target and returning -1 on not found
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
print(s.search([-1, 0, 3, 5, 9, 12], 2))
