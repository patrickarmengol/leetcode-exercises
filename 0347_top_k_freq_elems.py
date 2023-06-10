"""
neetcode - arrays & hashing - 5

sol 1: O(nlogn)
count with a counter and sort to return most common

sol 2: O(klogn)
count and use a heap to pop most common

sol 3: O(n)
use bucket sort to pop an array where index is count and values are the nums
"""
from collections import Counter

# most_common() uses sorted(self.items, key=itemgetter(1), reverse=True)
# most_common(k) uses heapq.nlargest(k, self.items, key=itemgetter(1))
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         c = Counter(nums)
#         return [a for a, _ in c.most_common(k)]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count.setdefault(n, 0)
            count[n] += 1
        for n, c in count:
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
