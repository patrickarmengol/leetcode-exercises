class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        for i in range(len(words)):
            if words[(startIndex + i) % len(words)] == target or words[startIndex - i] == target:
                return i
        return -1
