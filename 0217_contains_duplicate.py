"""
neetcode - arrays & hashing - 1

sol 1:
compare length of nums and its potentially deduplicated set

sol 2:
iterate through the list checking if cur in set, then adding
"""


# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         return len(set(nums)) != len(nums)


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return False
            else:
                s.add(n)
        return True
