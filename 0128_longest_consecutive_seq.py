class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        snums = set(nums)
        longest = 0
        for i in snums:
            if (i - 1) not in snums:  # start of sequence
                streak = 1
                while (i + streak) in snums:
                    streak += 1
                longest = max(longest, streak)
        return longest
