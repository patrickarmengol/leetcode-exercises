"""
neetcode - arrays & hashing - 3

sol 1: O(n**2)
brute force

sol 2: O(n)
dict to record previously seen n
enumerate, calc difference needed to reach target, check prevmap for diff
"""

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return [0, 0]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff], i]
            else:
                prevmap[n] = i
        return [0, 0]
