class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            even = mid % 2 == 0
            if nums[mid] == nums[mid + 1]:
                if even:
                    lo = mid + 1
                else:
                    hi = mid
            elif nums[mid - 1] == nums[mid]:
                if even:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]


s = Solution()
print(s.singleNonDuplicate([1, 1, 2, 2, 3, 4, 4]))
print(s.singleNonDuplicate([1]))
print(s.singleNonDuplicate([1, 1, 2]))


"""
could simplify this by only looking at even indeces
"""
