"""
neetcode - stacks - 4

sol 1:
brute force

sol 2:
recursively reach the end by
appending left when open < n
appending right when closed < open
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        results: list[str] = []
        stack: list[str] = []

        def backtrack(open: int, closed: int) -> None:
            if open == closed == n:
                results.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()

        backtrack(0, 0)

        return results
