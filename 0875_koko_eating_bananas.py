"""
neetcode - binary search - 3

sol:
check possible k, but use bin search to speed up
"""

import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        res = max(piles)
        left = 1
        right = res
        while left <= right:
            mid = (left + right) // 2
            s = sum((math.ceil(p / mid) for p in piles))
            if s <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res


s = Solution()
print(s.minEatingSpeed([3, 6, 7, 11], 8))
print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))
print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))
