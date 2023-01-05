class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return str(0)
        digits: list[str] = []
        while columnNumber:
            digits.append(chr((columnNumber-1) % 26 + 65))
            columnNumber = (columnNumber-1) // 26
        return ''.join(digits[::-1])
