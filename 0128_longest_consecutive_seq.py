"""
neetcode - arrays & hashing - 8

sol 1:
iterate through set of nums
start counting streak where n-1 not in set
compare streaks for max
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        snums = set(nums)
        longest = 0
        for n in snums:
            if (n - 1) not in snums:  # start of sequence
                streak = 1
                while (n + streak) in snums:
                    streak += 1
                longest = max(longest, streak)
        return longest
