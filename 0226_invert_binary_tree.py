class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    # recurse down the tree swapping children
    if root:
        root.left, root.right = root.right, root.left
        invert_tree(root.left)
        invert_tree(root.right)
    return root



# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root:
#             root.left, root.right = root.right, root.left
#             self.invertTree(root.left)
#             self.invertTree(root.right)
#         return root