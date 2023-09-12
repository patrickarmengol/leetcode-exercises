"""
neetcode - backtracking - 3

sol:
recurs with 2 lists; one for current combo, other for remaining in nums
when remaining is empty, append to result
else iterate through remaining and recurse with current union r[i] and r without r[i]
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(c: list[int], r: list[int]) -> None:
            if not r:
                res.append(c)
                return
            for i in range(len(r)):
                dfs(c + [r[i]], r[:i] + r[i + 1 :])

        dfs([], nums[:])
        return res
