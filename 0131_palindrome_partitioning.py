class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res: list[list[str]] = []

        def extend(i: int, cur: list[str]) -> None:
            # when start pointer reaches end of str, append to res
            if i >= len(s):
                res.append(cur[::])  # copy of cur

            # check all potential partitions in s[i:]
            p = ''
            for j in range(i, len(s)):
                p += s[j]
                if p == p[::-1]:  # check palindrome
                    extend(j + 1, cur + [p])  # once pal is found, recurse the rest

        extend(0, [])
        return res


"""
i tried, but couldn't get this sol on my own
hopefully backtracking becomes more clear to me soon
"""
