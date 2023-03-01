class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n >= i:
            n -= i
            i += 1
        return i - 1


tests = [
    5, 8, 1, 3
]

s = Solution()
for test in tests:
    print(s.arrangeCoins(test))

"""
apparently there is a binary search sol
"""
