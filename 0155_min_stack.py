"""
neetcode - stacks - 2
"""


# class MinStack:
#     def __init__(self):
#         self.stack: list[int] = []
#         self.minimum: list[int] = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if not self.minimum:
#             self.minimum.append(0)
#         else:
#             if val < self.stack[self.minimum[-1]]:
#                 self.minimum.append(len(self.stack) - 1)
#
#     def pop(self) -> None:
#         if self.minimum[-1] == len(self.stack) - 1:
#             self.minimum.pop()
#         self.stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.stack[self.minimum[-1]]


class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.minimum: list[int] = []

    def push(self, val: int) -> None:
        # push the val to stack
        self.stack.append(val)
        # push the min to minstack
        m = min(val, self.minimum[-1]) if self.minimum else val
        self.minimum.append(m)

    def pop(self) -> None:
        # pop from both stacks
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
