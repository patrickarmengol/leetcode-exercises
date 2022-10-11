import math
import heapq

def min_stone_sum(piles, k):
    piles = [-p for p in piles]
    heapq.heapify(piles)
    for _ in range(k):
        p = -heapq.heappop(piles)
        p -= math.floor(p / 2)
        heapq.heappush(piles, -p)
    return -sum(piles)


def main():
    print(min_stone_sum([5, 4, 9], 2))
    print(min_stone_sum([4, 3, 6, 7], 3))


if __name__ == '__main__':
    main()


"""
learned how to implement a max heap with heapq
i could have used heapreplace(piles[0], math.floor(p / 2))
"""