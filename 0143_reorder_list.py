"""
neetcode - linked list - 3

my initial solution utilized a deque to pop alternatively from each end
neetcode solution plays with the ll directly

sol1:
iterate over list and place nodes in deque
pop from both ends alternatively into new list

sol2: O(1) mem
use slow/fast pointers to find midpoint
break the midpoint
reverse the second half
merge the two halves
"""

from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head:
            return

        a = deque()
        while head:
            a.append(head)
            head = head.next

        n = None
        b = False
        while a:
            p = a.pop() if b else a.popleft()
            b = not b
            if not n:
                n = p
            else:
                n.next = p
                n = n.next
        if n:
            n.next = None


class OtherSolution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head:
            return
        slow = head
        fast = head.next
        # find middle of list
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # break mid and reverse second half
        if not slow:
            raise Exception("wtf")
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halves
        first = head
        second = prev
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


s = Solution()
ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
s.reorderList(ll)
while ll:
    print(f"{ll.val} -> ", end="")
    ll = ll.next
print("None")
