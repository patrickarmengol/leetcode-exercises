# all digits in n need to be 1 and n needs to be divisble by k
# probably faster to add a digit than accumulate by k

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        n = 0
        while True:
            n = n * 10 + 1
            if n % k == 0:
                return len(str(n))
