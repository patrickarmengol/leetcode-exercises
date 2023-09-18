"""
neetcode - heap / priority queue - 3

sol:
calculate distance values and save to new list of tuples (dist, point)
heapify list, by default uses dist to compare
return k pops from heap
"""

import math
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # create new list with tuple of dist, point
        heap = [
            (math.sqrt((points[i][0] - 0) ** 2 + (points[i][1] - 0) ** 2), points[i])
            for i in range(len(points))
        ]
        # heapify new list based on dist values
        heapq.heapify(heap)

        # pop k from heap
        return [heapq.heappop(heap)[1] for _ in range(k)]
