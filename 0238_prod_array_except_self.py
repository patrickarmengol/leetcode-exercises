"""
neetcode - arrays & hashing - 6

sol 1: O(n**2)
new array with each elem a product of values at all other indeces of orig

sol 2: O(n)
left to right then right to left; multiply result val by a rolling prev product
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
