"""
neetcode - trees - 13

sol:
iterate through the preorder with cur
find the index of cur in inorder
split array left right of that index
recurse with preorder list and both sides
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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        # pop left from preorder
        cur = preorder.pop(0)
        cur_node = TreeNode(cur)

        i = inorder.index(cur)
        left = inorder[:i]
        right = inorder[i + 1 :]

        if len(left) + len(right) == 0:
            return cur_node

        cur_node.left = self.buildTree(preorder, left)
        cur_node.right = self.buildTree(preorder, right)
        return cur_node
