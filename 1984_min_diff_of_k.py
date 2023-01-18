class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        snums = sorted(nums, reverse=True)
        md = 10 ** 5 + 1
        for i in range(len(snums) - (k - 1)):
            diff = snums[i] - snums[i + k - 1]
            if diff < md:
                md = diff
        return md
