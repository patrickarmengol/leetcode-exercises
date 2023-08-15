"""
neetcode - binary search - 2

sol:
bisect right along 0th column
grab row before insert point
binary search along row to find target
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix)
        while lo < hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target:
                lo = mid + 1
            else:
                hi = mid
        row = matrix[lo - 1]
        lo = 0
        hi = len(row)
        while lo < hi:
            mid = (lo + hi) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return False


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(s.searchMatrix([[1], [3]], 1))
