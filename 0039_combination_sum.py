"""
neetcode - backtracking - 2

sol:
explore all paths recursively
keepe track off combo list and combo sum
if the sum of the combo == target, append to result
if i is out of bounds return
explore path with same candidate as current
pop and explore path with next candidate
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i: int, combo: list[int], total: int) -> None:
            if total == target:
                res.append(combo[:])
                return
            if i >= len(candidates) or total > target:
                return

            combo.append(candidates[i])
            dfs(i, combo, total + candidates[i])

            combo.pop()
            dfs(i + 1, combo, total)

        dfs(0, [], 0)
        return res


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
