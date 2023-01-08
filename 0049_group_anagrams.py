
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d: dict[str, list[str]] = {}

        for s in strs:
            k = str(sorted(s))
            d.setdefault(k, [])
            d[k].append(s)
        return list(d.values())


"""
can speed up by using a char count array as key instead of sorted string
"""
