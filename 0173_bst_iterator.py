from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode | None):
        def rdfs(node: TreeNode | None, inorder: list[int] = []):
            if not node:
                return inorder
            rdfs(node.left, inorder)
            inorder.append(node.val)
            rdfs(node.right, inorder)
            return inorder
        self.i = -1
        self.order = rdfs(root)

    def next(self) -> int:
        if self.hasNext():
            self.i += 1
            return self.order[self.i]

    def hasNext(self) -> bool:
        return len(self.order) > self.i + 1
