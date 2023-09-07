"""
neetcode - sliding window - 5

sol:
count chars in t
use two pointers for sliding window
expand right until window has all needed in ct
contract left until window doesn't, updating min
"""

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = defaultdict(int)
        cc = defaultdict(int)

        for char in t:
            ct[char] += 1
            cc[char] = 0

        have = 0
        need = len(ct)
        i = 0
        j = 0
        ml = len(s)
        ms = ""
        while True:
            # expand right until substring has at least all in ct
            while have < need:
                if j >= len(s):
                    return ms
                if s[j] in ct:
                    cc[s[j]] += 1
                    if cc[s[j]] == ct[s[j]]:
                        have += 1

                j += 1
            # reduce left
            while have >= need:
                if j - i <= ml:
                    ml = j - i
                    ms = s[i:j]
                if s[i] in ct:
                    if cc[s[i]] == ct[s[i]]:
                        have -= 1
                    cc[s[i]] -= 1
                i += 1


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print()
print(s.minWindow("a", "a"))
print()
print(s.minWindow("a", "aa"))
print()
print(s.minWindow("ab", "a"))
print()
print(s.minWindow("aa", "aa"))
