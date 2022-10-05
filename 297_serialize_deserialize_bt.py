import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         def dfs_ser(node, seq):
#             if node:
#                 seq.append(str(node.val))
#                 dfs_ser(node.left, seq)
#                 dfs_ser(node.right, seq)
#             else:
#                 seq.append('null')
#             return seq
#         preorder = dfs_ser(root, [])
#         while preorder and preorder[-1] == 'null':
#             preorder.pop()
#         return '[' + ','.join(preorder) + ']'
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         if data == '[]':
#             return None

#         def build_tree(lq):
#             node_val = lq.pop() if lq else None
#             if node_val is None:
#                 return None
#             else:
#                 node = TreeNode(node_val)
#                 node.left = build_tree(lq)
#                 node.right = build_tree(lq)
#                 return node

#         preorder = [int(val) if val != 'null' else None for val in data.strip('[]').split(',')]
#         preorder_queue = preorder[::-1] # pop from end
#         return build_tree(preorder_queue)
                


            
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        bfs_order = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node:
                bfs_order.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                bfs_order.append('null')
        
        while bfs_order and bfs_order[-1] == 'null':
            bfs_order.pop()
        return '[' + ','.join(bfs_order) + ']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == '[]':
            return None
        
        bfs_order = [int(val) if val != 'null' else None for val in data.strip('[]').split(',')][::-1]
        queue = collections.deque()
        root = TreeNode(bfs_order.pop())
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            if bfs_order:
                left_val = bfs_order.pop()
                node.left = TreeNode(left_val) if left_val is not None else None
                queue.append(node.left)
            if bfs_order:
                right_val = bfs_order.pop()
                node.right = TreeNode(right_val) if right_val is not None else None
                queue.append(node.right)

        return root
                



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

def main():
    # ser = Codec()
    # deser = Codec()
    # root = deser.deserialize('[1,2,3,null,null,4,5]')
    # check = ser.serialize(root)
    # print(check)
    # ans = deser.deserialize(ser.serialize(root))
    # print(ans)

    ser = Codec()
    deser = Codec()
    root = deser.deserialize('[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]')
    check = ser.serialize(root)
    print(check)
    ans = deser.deserialize(ser.serialize(root))
    print(ans)


if __name__ == '__main__':
    main()