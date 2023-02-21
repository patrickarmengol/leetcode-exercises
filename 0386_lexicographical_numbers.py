class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        return sorted([i for i in range(1, n + 1)], key=str)
