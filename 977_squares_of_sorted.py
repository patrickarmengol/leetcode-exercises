def sorted_squares(nums):
    squares = []
    p = 0
    while p < len(nums) and nums[p] < 0:
        p += 1
    n = p-1
    while len(squares) < len(nums):
        left = -nums[n] if n >= 0 else float('inf')
        right = nums[p] if p < len(nums) else float('inf')
        if left <= right:
            squares.append(left ** 2)
            n -= 1
        else:
            squares.append(right ** 2)
            p += 1
    return squares

def main():
    for test in [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [4],
        [-1]
    ]:
        print(sorted_squares(test))


if __name__ == '__main__':
    main()


"""
another way that doesn't involve finding the neg/pos split at the start
use two pointers starting on the outside and work inwards comparing for greater of abs
use a deque to hold answers and append from left

def sortedSquares(self, A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)
"""