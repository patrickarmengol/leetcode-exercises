"""
neetcode - two pointers - 5

sol:
two pointers
iterate lowest bar
find new max for that side
accumulate water based on difference between max of that side and current bar height
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        lm = height[i]
        rm = height[j]
        water = 0
        while i < j:
            if lm < rm:
                i += 1
                lm = max(lm, height[i])
                water += lm - height[i]
            else:
                j -= 1
                rm = max(rm, height[j])
                water += rm - height[j]
        return water


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(s.trap([4, 2, 0, 3, 2, 5]))
