"""
neetcode - heap / priority queue - 6

sol:
get all posts from followed
use a heap to sort items by creation time
pop at most 10 from heap for result

neetcode solution is more efficient since only one most recent
"""

from collections import defaultdict, deque
import heapq


class Twitter:
    def __init__(self):
        self.count = 0
        # map users to posts
        self.posts = defaultdict(deque)
        # map users to followed
        self.followed = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].appendleft((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # add self to followed to see own posts in feed
        self.followed[userId].add(userId)

        # throw all followed posts into max heap (count as key)
        heap = []
        for followeeId in self.followed[userId]:
            if followeeId in self.posts:
                for post in self.posts[followeeId]:
                    heapq.heappush(heap, post)

        # pop at most 10 from heap and return
        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)


t = Twitter()
t.postTweet(1, 5)
t.postTweet(1, 3)
print(t.getNewsFeed(1))
