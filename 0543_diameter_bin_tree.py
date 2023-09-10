"""
neetcode - trees - 3

sol:
recursive max depth of each side
keep track of largest sum of left+right depths as you go down the tree
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
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        res = 0

        def dfs(node: TreeNode | None) -> int:
            nonlocal res

            if not node:
                return 0

            ld = dfs(node.left)
            rd = dfs(node.right)

            res = max(res, ld + rd)

            return max(ld, rd) + 1

        dfs(root)
        return res
