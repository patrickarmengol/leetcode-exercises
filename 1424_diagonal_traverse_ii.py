from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        buckets: dict[int, list[int]] = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                buckets[i + j].append(nums[i][j])
        m = max(buckets.keys())
        res: list[int] = []
        for b in range(m + 1):
            res.extend(reversed(buckets[b]))
        return res
