"""
neetcode - sliding window - 6

sol:
use a monotonically decreasing queue
keep left/right pointers for window
for as long as r is in bounds do the following
pop from right of queue until elem pointed to by r is <= the last elem in queue
append r
if left pointer is greater than pointer at start of queue, pop left
append the elemn pointed by start of the queue to result
increment l and r
"""
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = deque()
        left = 0
        right = 0

        while right < len(nums):
            # pop from right until new val is <=
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # l out of bounds
            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                res.append(nums[q[0]])
                left += 1
            right += 1

        return res
