"""
neetcode - linked list - 1

sol:
use python's handy simultaneous assignment
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        while head:
            head.next, head, prev = prev, head.next, head
        return prev
