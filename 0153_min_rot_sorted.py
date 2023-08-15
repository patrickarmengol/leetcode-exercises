"""
neetcode - binary search - 4

sol:
use binary search
if sorted, res is min of left and seen
if mid in higher portion, try to go to right
if mid in lower portion, try to reduce
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[right]
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res


s = Solution()
tests = (
    [3, 4, 5, 1, 2],
    [4, 5, 6, 7, 0, 1, 2],
    [11, 13, 15, 17],
)
for test in tests:
    print(s.findMin(test))
