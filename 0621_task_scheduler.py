"""
neetcode - heap / priority queue - 5

sol:
count letters
put counts into max heap
keep a queue, keep time

while heap or queue:
increment time
pop from heap and decrement count
push count to queue if not zero, with ready time
pop from queue and push to heap if ready
"""

from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # get counts of each letter
        c = Counter(tasks)
        # put counts in max heap
        heap = [-cnt for cnt in c.values()]
        heapq.heapify(heap)
        # keep queue of popped from heap to await idle finish
        q: deque[tuple[int, int]] = deque()

        time = 0
        while heap or q:
            time += 1

            if heap:
                # pop and decrement count for elem in heap
                p = heapq.heappop(heap)
                p += 1
                # if count, push to queue with ready time
                if p != 0:
                    q.append((p, time + n))  # ready time == current time + idle time

            # if ready time has been reached on first in queue
            if q and q[0][1] == time:
                # push back onto heap
                heapq.heappush(heap, q.popleft()[0])

        return time
