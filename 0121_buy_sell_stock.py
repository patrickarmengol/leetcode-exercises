"""
neetcode - sliding window - 1

sol:
iterate through prices and update minimum
track max difference between minimum and current price
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lastmin = prices[0]
        maxdiff = 0
        for price in prices[1:]:
            if price < lastmin:
                lastmin = price
            else:
                maxdiff = max(maxdiff, price - lastmin)
        return maxdiff


tests = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1]]

s = Solution()
for test in tests:
    print(s.maxProfit(test))
