"""
neetcode - two pointers - 4

sol:
two pointers
calc area defined by space between bars and compare to largest
move pointer at lower bar
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        largest = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            largest = max(area, largest)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return largest


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(s.maxArea([1, 1]))
