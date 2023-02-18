class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        while l < r:
            mid = (l + r) // 2
            if sum([(n - 1) // mid for n in nums]) > maxOperations:
                l = mid + 1
            else:
                r = mid
        return l
