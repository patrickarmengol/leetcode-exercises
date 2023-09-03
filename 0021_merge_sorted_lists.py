"""
neetcode - linked list - 2

sol:
iteratively compare lists and add nodes to new list
keep track of head for return
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        node = ListNode()
        result = node

        # compare min of lists and create node in res list
        while list1 and list2:
            if list1.val < list2.val:
                node.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val, None)
                list2 = list2.next
            node = node.next

        # leftover list gets stuck to tail
        node.next = list1 if list1 else list2

        return result.next
