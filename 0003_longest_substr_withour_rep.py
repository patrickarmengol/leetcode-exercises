"""
neetcode - sliding window - 2

sol:
use two pointers
right expands to include new characters
left shrinks until newest right char is unique
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        uc = set()
        longest = 0
        for right in range(len(s)):
            while s[right] in uc:
                uc.remove(s[left])
                left += 1
            uc.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
