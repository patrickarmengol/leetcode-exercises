"""
neetcode - trees - 5

sol:
recurse if p and q are same val
end case is p and q are None
if difference encountered, return False
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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


# class Solution:
#     def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
#         # iterative dfs is probably fine
#         sp, sq = [p], [q]
#         while sp and sq:
#             vp, vq = sp.pop(), sq.pop()
#             vpv = vp.val if vp else None
#             vqv = vq.val if vq else None
#             if vpv != vqv:
#                 return False
#             if vp and vq:
#                 sp.extend([vp.left, vp.right])
#                 sq.extend([vq.left, vq.right])
#         return True
