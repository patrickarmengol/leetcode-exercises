"""
neetcode - backtracking - 7

sol:
iterate through the list with i
when i reaches end of list, append copy of cur partitioning to result
for each start i, iterate j to end
if s[i:j+1] is palindrome, recurse with j + 1 as i and extend cur

"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res: list[list[str]] = []

        def extend(i: int, cur: list[str]) -> None:
            # when start pointer reaches end of str, append to res
            if i >= len(s):
                res.append(cur[::])  # copy of cur
                return

            # check all potential partitions in s[i:]
            p = ""
            for j in range(i, len(s)):
                p += s[j]
                if p == p[::-1]:  # check palindrome
                    extend(j + 1, cur + [p])  # once pal is found, recurse the rest

        extend(0, [])
        return res
