"""
neetcode - trees - 11

* watch vid *

sol:
recursive dfs
check if node val is between certain other vals
left and right bounds are intially +/- inf
if going left: right bound is reassigned to parent val
if going right: left bound is reassigned to parent val
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
    def isValidBST(self, root: TreeNode | None) -> bool:
        def valid(node: TreeNode | None, left: int | float, right: int | float):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            else:
                return valid(node.left, left, node.val) and valid(
                    node.right, node.val, right
                )

        return valid(root, float("-inf"), float("inf"))
