"""
neetcode - backtracking - 9

sol:
initialize board and keep track of results
backtrack func taking row
if row reached end, append to result
else iterate through columns
if r,c is valid, update sets and recurse on next row
once returned update sets back
"""

from pprint import pprint


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # instead of checking each col and diag for each new q
        # keep track of sets of occupied col and diag
        col = set()
        # diags can be encoded with (r + c) for forward, (r - c) for backward
        fdiag = set()
        bdiag = set()

        # initialise result and board
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        # recurse through rows, invalidating prev row for recursive call
        def backtrack(r: int) -> None:
            # reach end of board, append to result
            if r == n:
                res.append(["".join(row) for row in board])
                return

            # start at first col every new row
            for c in range(n):
                # check invalid
                if c in col or (r + c) in fdiag or (r - c) in bdiag:
                    continue

                # potentially valid
                col.add(c)
                fdiag.add(r + c)
                bdiag.add(r - c)
                board[r][c] = "Q"

                # recurse on next row
                backtrack(r + 1)

                # undo adding to sets
                col.remove(c)
                fdiag.remove(r + c)
                bdiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


s = Solution()
pprint(s.solveNQueens(1))
pprint(s.solveNQueens(2))
pprint(s.solveNQueens(3))
pprint(s.solveNQueens(4))
pprint(s.solveNQueens(5))
pprint(s.solveNQueens(6))
pprint(s.solveNQueens(7))
