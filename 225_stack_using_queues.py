import collections

class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.appendleft(self.q.pop())
        return self.q.pop()

    def top(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.appendleft(self.q.pop())
        t = self.q.pop()
        self.q.appendleft(t)
        return t

    def empty(self) -> bool:
        return len(self.q) == 0

def main():
    ms = MyStack()
    ms.push(1)
    ms.push(2)
    print(ms.top())
    print(ms.pop())
    print(ms.top())
    print(ms.empty())
    print(ms.pop())
    print(ms.empty())

if __name__ == '__main__':
    main()


"""
Runtime: 56 ms, faster than 34.97% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 14 MB, less than 75.12% of Python3 online submissions for Implement Stack using Queues.

not much i could improve imo
top is O(n) since deque doesn't really have a peek; if it did, i would make push O(n) and pop + top O(1)
"""