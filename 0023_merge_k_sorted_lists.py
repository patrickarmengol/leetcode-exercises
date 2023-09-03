"""
neetcode - linked list - 10

my original solution iterated over the k lists to find min and pop to result list
too slow - O(k*n)

sol:
emulate merge sort
while more than one ll in lists, merge pairs of lists
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
#         dummy = ListNode()
#         node = dummy
#
#         while any(lists):
#             mi = -1
#             mv = float("inf")
#             for i, n in enumerate(lists):
#                 if n and n.val < mv:
#                     mi = i
#                     mv = n.val
#             if not node or not lists[mi]:
#                 raise Exception("wtf")
#             node.next = lists[mi]
#             lists[mi] = lists[mi].next
#             node = node.next
#         return dummy.next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self._merge(l1, l2))
            lists = merged_lists
        return lists[0]

    def _merge(self, l1: ListNode | None, l2: ListNode | None):
        dummy = ListNode()
        node = dummy
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        node.next = l1 if l1 else l2
        return dummy.next
