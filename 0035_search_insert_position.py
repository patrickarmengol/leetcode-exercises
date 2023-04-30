class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


"""
really just using stdlib's bisect.bisect_left() as a reference
"""
