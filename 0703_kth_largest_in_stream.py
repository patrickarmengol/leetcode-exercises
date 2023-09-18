"""
neetcode - heap / priority queue - 1

sol:
keep track of heap from nums
heap needs to be size k, since small values don't matter
when heap size k, then heap[0] / heap's min is kth largest
for adding, push onto heap, pop to offset
then return heap[0]
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)
        # only need k elements in heap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # add new elem from stream
        heapq.heappush(self.heap, val)
        # pop from heap to offset
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # kth largest is min from heap (but don't pop)
        return self.heap[0]


asdf = KthLargest(3, [4, 5, 8, 2])
print(asdf.add(3))
print(asdf.add(5))
print(asdf.add(10))
print(asdf.add(9))
print(asdf.add(4))
