"""
neetcode - binary search - 7

sol (no way i was finding this myself):
do binary search on the shorter nums array
the midpoint marks the partition
compensate to reach half of total len with marker for longer array
check if the markers are valid partitioning points
median then depends on even or odd and is calculated with values at and next to markers
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) < len(nums2):
            a, b = nums1, nums2
        else:
            a, b = nums2, nums1

        left = 0
        right = len(a) - 1
        total_len = len(a) + len(b)
        half = total_len // 2

        while True:
            amid = (left + right) // 2
            bmid = half - amid - 2

            al = a[amid] if amid >= 0 else float("-infinity")
            ar = a[amid + 1] if (amid + 1) < len(a) else float("infinity")
            bl = b[bmid] if bmid >= 0 else float("-infinity")
            br = b[bmid + 1] if (bmid + 1) < len(b) else float("infinity")

            if al <= br and bl <= ar:
                if total_len % 2 != 0:
                    return min(ar, br)
                else:
                    return (max(al, bl) + min(ar, br)) / 2
            elif al > br:
                right = amid - 1
            else:
                left = amid + 1


s = Solution()
print(s.findMedianSortedArrays([1, 3], [2]))
print(s.findMedianSortedArrays([1, 2], [3, 4]))
