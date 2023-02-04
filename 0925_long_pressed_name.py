class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        if len(name) > len(typed):
            return False
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j-1] == typed[j]:
                j += 1
            else:
                return False
        return i == len(name) and all(name[-1] == x for x in typed[j-1:])


"""
absolutely disgusting
i just kept adding appendages to this code to fit all the edge cases
"""
