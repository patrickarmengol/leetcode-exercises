"""
neetcode - linked list - 5

sol:
iterate over the list, creating a copy node, and mapping orig to copy nodes
iterate again to assign each nodes next and random based on lookups in map

note:
my original solution was the same concept, except I assigned next on the first iteration
"""
from __future__ import annotations


class Node:
    def __init__(self, x: int, next: Node | None = None, random: Node | None = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        d: dict[Node | None, Node | None] = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val, None, None)
            d[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = d[cur]
            if copy is None:
                raise Exception("wtf")
            copy.next = d[cur.next]
            copy.random = d[cur.random]
            cur = cur.next

        return cur
