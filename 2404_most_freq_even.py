class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        d: dict[int, int] = {}
        f = (-1, -1)
        for n in nums:
            if n % 2 == 0:
                d.setdefault(n, 0)
                d[n] += 1
                if d[n] > f[1] or (d[n] == f[1] and n < f[0]):
                    f = (n, d[n])
        return f[0]
