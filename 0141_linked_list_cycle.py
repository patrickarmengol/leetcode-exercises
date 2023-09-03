"""
neetcode - linked list - 7

sol1:
use a set or hashmap to check if node has been visited

sol2: O(1) mem
use slow/fast pointers
if there is a loop, fast will eventually collide with slow
if there isn't a loop, fast will reach null
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False


class OtherSolution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
