class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif stack and c in ')]}':
                p = stack.pop()
                if ''.join((p, c)) not in '()[]{}':
                    return False
            else:
                return False
        return not stack
