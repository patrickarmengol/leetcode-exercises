class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.minimum: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(0)
        else:
            if val < self.stack[self.minimum[-1]]:
                self.minimum.append(len(self.stack) - 1)

    def pop(self) -> None:
        if self.minimum[-1] == len(self.stack) - 1:
            self.minimum.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.minimum[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


"""
cleaner solution that appends min val to minstack for each push instead of an index when new min is found

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

"""
