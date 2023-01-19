import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log2(n)
        return x - math.floor(x) < 0.00000000001


"""
cool bitwise logic
class Solution(object):
    def isPowerOfTwo(self, n):
        return n and not (n & n - 1)
"""
