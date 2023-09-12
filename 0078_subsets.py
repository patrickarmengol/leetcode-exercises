"""
neetcode - backtracking - 1

sol:
explore all paths recursively
i points to index in nums
choose to include nums[i] and recurse
then choose to exclude nums[i] and recurse
when i reaches end, append current subset to result and return
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        sub = []

        def dfs(i: int) -> None:
            # i went past end
            if i == len(nums):
                res.append(sub[:])
                return

            # include cur
            sub.append(nums[i])
            # recurse in that branch on next i
            dfs(i + 1)

            # exclude cur
            sub.pop()  # undo the append above
            # recurse in that branch on next i
            dfs(i + 1)

        dfs(0)
        return res
