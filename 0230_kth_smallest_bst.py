"""
neetcode - trees - 12

sol:
iterative inorder traversal, stopping at kth in sequence
"""

from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        s = []
        cur = root

        while cur or s:
            # go left til null
            while cur:
                s.append(cur)
                cur = cur.left
            # get top of stack / next smallest
            cur = s.pop()
            # decrement count
            k -= 1
            # check if kth in sequence
            if k == 0:
                return cur.val
            # go right
            else:
                cur = cur.right
        return -1  # should not happen
