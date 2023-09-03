"""
neetcode - linked list - 4

sol (for one pass):
use two pointers for slow/fast
move fast ahead n places
iterate slow and fast together until fast reaches end
remove slow

neetcode solution uses dummy pointer to help with deleting first node
can instead just return second node
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # move forward pointer ahead n times
        for _ in range(n):
            if not fast:
                raise Exception("wtf")
            fast = fast.next

        # if to_del is start of list
        if not fast:
            return head.next

        while fast.next and slow.next:
            fast = fast.next
            slow = slow.next

        # del next
        if not slow or not slow.next:
            raise Exception("wtf")
        slow.next = slow.next.next

        return head
