"""
neetcode - backtracking - 6

sol:
iterate through the the 2darr to find start point
call recursion at each potential start
recursion returns when ipointer reaches word len
if cur r, c is in bounds, and pointing to desired char
add to path
recurse with neighbors
remove from path
if any of the start points have a valid path, return True
else false
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        path = set()

        def dfs(r: int, c: int, i: int) -> bool:
            # if i reaches len(word), finished
            if i == len(word):
                return True
            # ensure r, c in boundds and pointing to desired letter and not visited
            if not (
                0 <= r < height
                and 0 <= c < width
                and board[r][c] == word[i]
                and (r, c) not in path
            ):
                return False
            path.add((r, c))
            # if one of the child paths is successful, the whole thing is
            res = (
                dfs(r - 1, c, i + 1)
                or dfs(r + 1, c, i + 1)
                or dfs(r, c - 1, i + 1)
                or dfs(r, c + 1, i + 1)
            )
            path.remove((r, c))
            return res

        # find start
        for r in range(height):
            for c in range(width):
                # recurse
                if dfs(r, c, 0):
                    return True
        return False


s = Solution()
print(
    s.exist(
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"
    )
)
