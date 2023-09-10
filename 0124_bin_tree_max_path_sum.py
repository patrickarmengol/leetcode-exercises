"""
neetcode - trees - 14

sol:
recurse down tree with dfs
if node null -> return 0
find dfs of left and right children
floor return to 0 since we want to exclude negatives
update result with split max
return single branch max
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
    def maxPathSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        res = root.val

        def dfs(node: TreeNode | None) -> int:
            nonlocal res
            if node is None:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # max path sum with split
            res = max(res, node.val + left + right)

            # max path sum without split
            return node.val + max(left, right, 0)

        dfs(root)
        return res
