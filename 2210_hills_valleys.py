class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        snums: list[int] = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                snums.append(nums[i])
        count = 0
        for i in range(1, len(snums)-1):
            if snums[i-1] < snums[i] and snums[i+1] < snums[i]:
                count += 1
            elif snums[i-1] > snums[i] and snums[i+1] > snums[i]:
                count += 1
        return count


"""
found another solution that just dealt with repeating values in a clever way

def countHillValley(self, nums: List[int]) -> int:
    hillValley = 0
    for i in range(1, len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = nums[i-1]
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:     #hill check
            hillValley += 1
        if nums[i] < nums[i-1] and nums[i] < nums[i+1]:     #valley check
            hillValley += 1
    return hillValley
"""
