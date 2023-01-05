from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = (l1, l2)
        s = ListNode()
        cs = s
        carry = 0
        while c1 or c2 or carry:
            cs.next = ListNode()
            cs = cs.next
            currentdigit = (c1.val if c1 else 0) + (c2.val if c2 else 0) + carry
            carry = currentdigit // 10
            remainder = currentdigit % 10
            cs.val = remainder
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None
        return s.next
