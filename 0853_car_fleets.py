"""
neetcode - stacks - 6

sol:
sort cars by position
iterate and push to stack; if car will catch up to the one in front, pop it from stack
"""


# class Solution:
#     def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
#         n_fleets = len(position)
#         steps: list[float] = []
#         ps = sorted(zip(position, speed))
#         for car in ps:
#             steps.append((target - car[0]) / car[1])
#         for i in range(len(steps) - 1, 0, -1):
#             if steps[i] >= steps[i - 1]:
#                 steps[i - 1] = steps[i]
#                 n_fleets -= 1
#         return n_fleets


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        steps: list[float] = []
        ps = sorted(zip(position, speed), reverse=True)
        for p, s in ps:
            steps.append((target - p) / s)
            if len(steps) >= 2 and steps[-1] <= steps[-2]:
                steps.pop()
        return len(steps)
