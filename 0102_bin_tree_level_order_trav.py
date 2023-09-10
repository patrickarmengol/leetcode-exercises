"""
neetcode - trees - 8

sol:
bfs, emptying the queue for each level
all elements of each level added to result
"""

from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        q = deque()
        if root:
            q.append(root)
        res: list[list[int]] = []

        while True:
            level: list[int] = []
            nq = deque()
            while q:
                v = q.popleft()
                if not v:
                    continue
                level.append(v.val)
                if v.left:
                    nq.append(v.left)
                if v.right:
                    nq.append(v.right)
            res.append(level)
            if len(nq) == 0:
                return res
            else:
                q = nq
