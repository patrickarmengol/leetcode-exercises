class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        n_fleets = len(position)
        steps: list[float] = []
        ps = sorted(zip(position, speed))
        for car in ps:
            steps.append((target - car[0]) / car[1])
        for i in range(len(steps)-1, 0, -1):
            if steps[i] >= steps[i-1]:
                steps[i-1] = steps[i]
                n_fleets -= 1
        return n_fleets


"""
can also keep steps in a stack and limit space complexity by popping from stack each new fleet
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

"""
