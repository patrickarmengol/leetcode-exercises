from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], left: bool) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                if left:
                    return node.val
                else:
                    return 0
            else:
                return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)
