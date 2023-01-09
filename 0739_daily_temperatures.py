class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[int] = []
        answer: list[int] = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                p = stack.pop()
                answer[p] = i - p
            stack.append(i)
        return answer
