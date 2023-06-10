"""
neetcode - arrays & hashing - 4

sol 1:
use sorted strings as bucket keys

sol 2:
use char counters as bucket keys
"""

from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         d: defaultdict[str, list[str]] = {}
#
#         for s in strs:
#             k = str(sorted(s))
#             d[k].append(s)
#         return list(d.values())


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d: defaultdict[tuple[int], list[str]] = defaultdict(list[str])

        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            d[tuple(counter)].append(s)

        return list(d.values())
