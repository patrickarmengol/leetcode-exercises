"""
neetcode - stacks - 7

sol:
pop from stack when cur bar height is lower than top of stack and calc max area of pop
push new bar to stack with how far it stretches left
at end check the rest of the stack that stretches all the way right
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack: list[tuple[int, int]] = []
        largest = 0

        for i, h in enumerate(heights):
            start = i
            # if height is lower than top of stack, pop top and calc max area
            while stack and h < stack[-1][1]:
                pi, ph = stack.pop()
                largest = max(largest, ph * (i - pi))
                start = pi
            # start index is how far left it stretches
            stack.append((start, h))

        # leftover ascending
        # each stretch to end
        for i, h in stack:
            largest = max(largest, h * (len(heights) - i))

        return largest
