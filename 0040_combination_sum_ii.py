"""
neetcode - backtracking - 5

sol:
combine solutions from 0039 and 0090
keep track of combo list and combo sum
if sum of combo == target, append to result
if i ins out of bounds or sum gt target return
explore path with next including cur
pop and ensure next is not same as cur
explore path with next excluding cur
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def dfs(i: int, combo: list[int], total: int) -> None:
            # add to result if equal
            if total == target:
                res.append(combo[:])
                return
            # went past end or gt target
            if i >= len(candidates) or total > target:
                return

            # path with cur
            combo.append(candidates[i])
            dfs(i + 1, combo, total + candidates[i])

            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, combo, total)

        dfs(0, [], 0)
        return res


sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(sol.combinationSum2([2, 5, 2, 1, 2], 5))
