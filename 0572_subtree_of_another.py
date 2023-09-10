"""
neetcode - trees - 6

i think recursion + closures causes slowdowns

sol:
iterate along tree with dfs and check same with same tree algo
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
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
            if not p and not q:
                return True
            elif p and q and p.val == q.val:
                return same_tree(p.left, q.left) and same_tree(p.right, q.right)
            else:
                return False

        if root:
            if same_tree(root, subRoot):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(
                    root.right, subRoot
                )
        else:
            return False

        # s = [root]
        # while s:
        #     v = s.pop()
        #     if v:
        #         if same_tree(v, subRoot):
        #             return True
        #         else:
        #             s.extend([v.left, v.right])
        # return False
