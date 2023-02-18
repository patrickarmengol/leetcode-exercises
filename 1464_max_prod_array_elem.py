class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        m1 = 0
        m2 = 0
        for n in nums:
            if n >= m1:
                if m1 > m2:
                    m2 = m1
                m1 = n
            elif n >= m2:
                m2 = n
        return (m1 - 1) * (m2 - 1)


s = Solution()
print(s.maxProduct([3, 4, 5, 2]))
