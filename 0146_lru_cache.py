"""
neetcode - linked list - 9

sol:
use a hashmap to map keys to nodes in doubly linked list
keep track of left right pointers for reference
nodes hold key, value pairs, and prev/next
when putting new element, insert into list from right
when putting exi element, remove from list and insert from right
when getting, remove from list and insert from right
"""


from __future__ import annotations


class ListNode:
    def __init__(
        self,
        key: int,
        val: int,
        prev: ListNode | None = None,
        next: ListNode | None = None,
    ):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()  # maps keys to nodes
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def _remove(self, node: ListNode):
        if not node.prev or not node.next:
            raise Exception("error removing")
        node.prev.next, node.next.prev = node.next, node.prev

    # insert node at right
    def _insert(self, node: ListNode):
        mru = self.right.prev
        if not mru:
            raise Exception("error inserting")
        mru.next = node
        self.right.prev = node
        node.prev = mru
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            # pop lru
            lru = self.left.next
            if not lru:
                raise Exception("wtf")
            self._remove(lru)
            del self.cache[lru.key]
