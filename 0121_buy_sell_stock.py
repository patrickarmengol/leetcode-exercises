class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lastmin = prices[0]
        maxdiff = 0
        for i in range(1, len(prices)):
            if lastmin < prices[i]:
                if prices[i] - lastmin > maxdiff:
                    maxdiff = prices[i] - lastmin
            else:
                lastmin = prices[i]
        return maxdiff


tests = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1]
]

s = Solution()
for test in tests:
    print(s.maxProfit(test))
