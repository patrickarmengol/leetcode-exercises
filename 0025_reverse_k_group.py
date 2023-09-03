"""
neetcode - linked list - 11

my implementation is quite different from neetcode's
but the concept is the same
diff is counting k elements to check len instead of re-reversing leftovers

sol:
reverse k elements and recurse the remainder list
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        # case where k is multiple of len
        if not head:
            return None

        # get a pointer to what will be the tail of the group
        orig = head

        # reverse the group
        prev = None
        for i in range(k):
            if head:
                head.next, head, prev = prev, head.next, head
            # case where k is not a multiple of len
            else:
                head = prev
                prev = None
                for j in range(i):
                    if not head:
                        raise Exception("wtf")
                    head.next, head, prev = prev, head.next, head
                return prev

        # set tail's next pointer to the result of a recursion
        orig.next = self.reverseKGroup(head, k)
        return prev


s = Solution()
print(
    s.reverseKGroup(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2
    )
)
