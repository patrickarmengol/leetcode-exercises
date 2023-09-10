"""
neetcode - trees - 7

sol:
check to see if root is inbetween
if not, go down tree
if root is < p and q, go right
if root is > p and q, go left
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
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        while True:
            if not root:
                raise Exception("wtf")
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
