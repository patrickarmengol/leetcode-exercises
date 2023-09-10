"""
neetcode - trees - 9

sol:
bfs, emptying the queue each level
last element in queue is added to result
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
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        q = deque()
        if root:
            q.append(root)
        res: list[int] = []

        while q:
            lq = len(q)
            for i in range(lq):
                v = q.popleft()
                if not v:
                    continue
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
                if i == lq - 1:
                    res.append(v.val)
        return res
