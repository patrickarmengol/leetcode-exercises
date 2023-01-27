class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        m = 0
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                m = max(m, j - i)
                j += 1
            else:
                i += 1
        return m
