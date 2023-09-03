"""
neetcode - linked list - 8

sol:
use slow/fast + floyd's algo
treat array vals as pointers to go to next instead of iterating
first find intersection
then increment two slow pointers until another intersection
second intersection is always the entrance of the cycle
"""


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0

        # find intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # find start of cycle
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow
