class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        orig = [first]
        for i, e in enumerate(encoded):
            orig.append(e ^ orig[i])
        return orig
