"""
neetcode - binary search - 5

sol:
use bin search
different rules for modifying left and right whether mid in higher or lower portion
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # if in high portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # if in low portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
print(s.search([1], 0))
