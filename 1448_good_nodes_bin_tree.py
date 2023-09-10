"""
neetcode - trees - 10

sol:
recursive dfs keeping track of path's max
if node val is >= pathmax, add 1 to result
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
    def goodNodes(self, root: TreeNode | None) -> int:
        def dfs(root: TreeNode | None, m: int) -> int:
            if not root:
                return 0
            else:
                nm = max(m, root.val)
                return (
                    dfs(root.left, nm)
                    + dfs(root.right, nm)
                    + (1 if m <= root.val else 0)
                )

        if not root:
            return 0
        return dfs(root, root.val)
