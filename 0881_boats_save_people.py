from collections import deque


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        d = deque(sorted(people, reverse=True))
        bcount = 0
        while d:
            l = d.popleft()
            rem = limit - l
            if d and d[-1] <= rem:
                d.pop()
            bcount += 1
        return bcount


"""
used deque instead of two pointers; some performance hit
"""
