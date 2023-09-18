"""
neetcode - heap / priority queue - 2

sol:
create a max heap by making each element negative, then heapifying
while there is more than 1 stone left:
    pop 2 into y and x
    if x < y, push the difference
return the negative of the remaining elem in heap
"""

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # create a maxheap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if y == x:
                continue
            else:
                heapq.heappush(heap, y - x)
        return -heap[0] if len(heap) > 0 else 0
