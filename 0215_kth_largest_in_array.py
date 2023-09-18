"""
neetcode - heap / priority queue - 4

a few solutions:
- sort and get kth elem from end
- create a max queue and pop k times
- quick select algorithm
"""

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)


# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         def partition(nums: list[int], left: int, right: int) -> int:
#             # pivot is right elem
#             pivot_val, fill = nums[right], left
#
#             # iterate through and swap values when...
#             for i in range(left, right):
#                 if nums[i] <= pivot_val:
#                     nums[fill], nums[i] = nums[i], nums[fill]
#                     fill += 1
#
#             nums[fill], nums[right] = nums[right], nums[fill]
#
#             return fill
#
#         # convert k to point to result
#         k = len(nums) - k
#         left, right = 0, len(nums) - 1
#
#         while left < right:
#             pivot = partition(nums, left, right)
#
#             if pivot < k:
#                 left = pivot + 1
#             elif pivot > k:
#                 right = pivot - 1
#             else:
#                 break  # found result
#
#         return nums[k]
