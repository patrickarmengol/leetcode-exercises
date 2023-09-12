"""
neetcode - backtracking - 4

sol:
similar to 0078
need to sort list
when going down right path (excluding) make sure next val is unique
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        sub = []

        def dfs(i: int) -> None:
            # i went past end
            if i == len(nums):
                res.append(sub[:])
                return

            # include cur
            sub.append(nums[i])
            dfs(i + 1)

            # exclude cur
            sub.pop()
            # increment i until new val
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res
