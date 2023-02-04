from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        i = 0
        while i <= len(s2) - len(s1):
            w = Counter(s2[i:i+len(s1)])
            if w == c:
                return True
            i += 1
        return False


"""
can avoid creating counter each time by removing left side of window and adding right
"""
