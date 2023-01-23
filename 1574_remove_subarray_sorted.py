class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        l = 0
        while l < len(arr) - 1 and arr[l] <= arr[l+1]:
            l += 1
        if l == len(arr) - 1:
            return 0
        r = len(arr) - 1
        while arr[r] >= arr[r-1]:
            r -= 1
        result = min(len(arr) - 1 - l, r)
        i = 0
        while i <= l and r < len(arr):
            if arr[i] > arr[r]:
                r += 1
            else:
                result = min(result, r - i - 1)
                i += 1
        return result
