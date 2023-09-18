"""
neetcode - heap / priority queue - 7

sol:
keep track of two heaps and balance their lengths
elements are sorted into heaps depending on val
if one heap has 2 more than the other, rebalance the heaps

result is either unbalanced elem from the longer heap or mean of edges of heaps
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.small_heap = []  # max heap
        self.large_heap = []  # min heap

    def addNum(self, num: int) -> None:
        # check which heap the new val should go in
        if self.large_heap and num > self.large_heap[0]:
            heapq.heappush(self.large_heap, num)
        else:
            heapq.heappush(self.small_heap, -num)

        # balance the heaps
        diff = len(self.small_heap) - len(self.large_heap)
        # small has +2 elem
        if diff == 2:
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))
        # large has +2 elem
        if diff == -2:
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))

    def findMedian(self) -> float:
        # median is unbalanced elem or mean of edges of heap
        diff = len(self.small_heap) - len(self.large_heap)
        # heaps are same size, take mean
        if diff == 0:
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        # small heap has +1 elem, take max elem from heap
        elif diff == 1:
            return -self.small_heap[0]
        # large heap has +1 elem, take min elem from heap
        else:
            return self.large_heap[0]
