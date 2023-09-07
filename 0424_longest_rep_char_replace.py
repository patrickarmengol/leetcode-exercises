"""
neetcode - sliding window - 3

sol:
window grows from start
increment right
if window valid (window size - # of most freq char <= k), update max
if window invalid, increment left until valid
most freq char can be calculated each time, or a var can track it kinda (wont decrement)
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        res = 0
        count = defaultdict(int)
        maxf = 0
        while right < len(s):
            count[s[right]] += 1
            maxf = max(maxf, count[s[right]])

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res
