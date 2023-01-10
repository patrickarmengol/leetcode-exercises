class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers)-1
        while (s := numbers[i] + numbers[j]) != target:
            if s < target:
                i += 1
            else:
                j -= 1
        return [i+1, j+1]
