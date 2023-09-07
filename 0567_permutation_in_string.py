"""
neetcode - sliding window - 4

sol:
count letters in s1
window along s2 of size s1 and count letters in window
if count of letters matches, return true
window counter changes so can add/sub from edges to avoid recalculating entire window
"""

from collections import Counter

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         c = Counter(s1)
#         i = 0
#         while i <= len(s2) - len(s1):
#             w = Counter(s2[i : i + len(s1)])
#             if w == c:
#                 return True
#             i += 1
#         return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2[: len(s1)])
        if c1 == c2:
            return True

        for i in range(len(s1), len(s2)):
            c2[s2[i - len(s1)]] -= 1  # decrement counter at left pointer
            c2[s2[i]] += 1  # increment counter at right pointer
            if c1 == c2:
                return True
        return False
