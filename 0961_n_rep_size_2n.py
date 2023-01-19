class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        s: set[int] = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)
