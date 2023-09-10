"""
neetcode - trees - 4

sol:
recursive depth closure
as recursing, check if difference in depth is greater than 1
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
    def isBalanced(self, root: TreeNode | None) -> bool:
        res = True

        def dfs(node: TreeNode | None) -> int:
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                res = False
            return max(left, right) + 1

        dfs(root)
        return res
