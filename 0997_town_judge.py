class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if not trust:
            if n == 1:
                return 1
            else:
                return -1
        pot = set(range(1, n+1))
        bc: dict[int, int] = {}
        for a, b in trust:
            if a in pot:
                pot.remove(a)
            bc.setdefault(b, 0)
            bc[b] += 1
        if not pot:
            return -1
        j = pot.pop()
        if bc[j] == n - 1:
            return j
        else:
            return -1


"""
absolutely ugly answer; just ended up stacking edge cases with logic instead fixing the alg
"""
