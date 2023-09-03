"""
neetcode - linked list - 6

sol:
iterate through both lists, summing digit-wise and calcing the carry
sumlist gets initiated with remainder vals
"""

from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        ls = dummy
        carry = 0
        while l1 or l2 or carry:
            cs = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = cs // 10
            remainder = cs % 10
            ls.next = ListNode(remainder)

            ls = ls.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
