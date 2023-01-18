class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        snums = sorted(nums)
        res: set[tuple[int, int, int]] = set()
        for k in range(1, len(snums)-1):
            i = 0
            j = len(snums) - 1
            while i < k < j:
                s = snums[i] + snums[j] + snums[k]
                if s == 0:
                    res.add((snums[i], snums[j], snums[k]))
                    if snums[i] - snums[i+1] < snums[j] - snums[j-1]:
                        i += 1
                    else:
                        j -= 1
                elif s > 0:
                    j -= 1
                else:
                    i += 1
        return [list(a) for a in res]


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
