import math


class Solution:
    def __init__(self):
        self.dp = [0] + [float('inf')] * (10 ** 4)

    def num_squares(self, n):
        if self.dp[n] <= n:
            print('asdf')
            return self.dp[n]

        for i in range(1, n + 1):
            self.dp[i] = min(self.dp[i - j ** 2]
                             for j in range(1, math.floor(math.sqrt(i)) + 1)) + 1

        return self.dp[n]


def main():
    s = Solution()
    print(s.num_squares(101))
    print(s.num_squares(100))
    print(s.num_squares(9))
    print(s.num_squares(402))
    print(s.num_squares(8935))


if __name__ == '__main__':
    main()

"""
hmm... i would have thought this solution was optimal
i even kept a persistent dp list to cheat and make future calls faster
i got TLE twice and accepted once without ever changing the code
"""
