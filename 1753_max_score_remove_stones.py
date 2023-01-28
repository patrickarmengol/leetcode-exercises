class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        s = a + b + c
        mi = min(a, b, c)
        ma = max(a, b, c)
        mm = s - ma - mi
        if ma >= mi + mm:
            return mi + mm
        else:
            return s // 2


"""
looking at example
a = 1, b = 8, c = 8
result is 8, which is sum // 2 as also seen in prev examples

but if you move stones from b to c
a = 1, b = 1, c = 15
result is 2, which is a + b

can check with 
a = 1, b = 2, c = 14
result is 3, which is a + b
"""
