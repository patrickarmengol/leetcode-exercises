class StockSpanner:

    def __init__(self):
        self.prices = []
        self.last_streak = 0

    def next(self, price: int) -> int:
        self.prices.append(price)
        i = len(self.prices) - 1
        streak = 0
        if len(self.prices) > 1 and price >= self.prices[-2]:
            streak += self.last_streak
            i -= streak
        while i >= 0:
            if price >= self.prices[i]:
                streak += 1
                i -= 1
            else:
                break
        self.last_streak = streak
        return streak


def main() -> None:
    ss = StockSpanner()
    print(ss.next(100))
    print(ss.next(80))
    print(ss.next(60))
    print(ss.next(70))
    print(ss.next(60))
    print(ss.next(75))
    print(ss.next(85))
        

if __name__ == '__main__':
    main()



"""
the leetcode provided solution took me a while to understand
my solution only skips back 1 streak, but then iterates from there bc it doesn't remember other streaks

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        
        self.stack.append([price, ans])
        return ans

"""