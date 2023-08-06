"""
neetcode - two pointers - 3

sol:
sort the list
k iterates through negative values and 0
i and j do two pointer and check sum == 0
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        snums = sorted(nums)
        res: set[tuple[int, int, int]] = set()
        for k in range(len(snums)):
            # skip positive integers
            if snums[k] > 0:
                break
            # skip duplicates
            elif k > 0 and snums[k] == snums[k - 1]:
                continue
            i = k + 1
            j = len(snums) - 1
            while i < j:
                s = snums[i] + snums[j] + snums[k]
                if s > 0:
                    j -= 1
                elif s < 0:
                    i += 1
                else:
                    res.add((i, j, k))
                    i += 1
                    j -= 1

        return [list(a) for a in res]


a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
