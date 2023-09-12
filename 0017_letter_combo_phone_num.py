"""
neetcode - backtracking - 8

my solution was almost exactly like the neetcode one

sol:
map digits to letters
keep track of result list
backtrack func
if reach end of digits, append current combo to result
else iterate through letters that i maps to and recurse
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        nl_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(i: int, combo: str) -> None:
            if i == len(digits):
                res.append(combo)
                return
            for letter in nl_map[digits[i]]:
                backtrack(i + 1, combo + letter)

        if digits:
            backtrack(0, "")
        return res
