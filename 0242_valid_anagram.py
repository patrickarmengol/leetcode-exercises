"""
neetcode - arrays & hashing - 2

sol 1: O(nlogn)
check if both strings sorted are equal

sol 2: O(n)
count each char in each string and compare counters
"""


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        return count_s == count_t
