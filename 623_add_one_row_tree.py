import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def serialize(root):
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
    

def deserialize(data):
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



class Solution:
    def addOneRow(self, root, val, depth):
        if root is None:
            return None
        
        if depth == 1:
            return TreeNode(val, root, None)

        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            node, d = queue.popleft()

            if node:
                if d == depth - 2:
                    node.left = TreeNode(val, node.left, None)
                    node.right = TreeNode(val, None, node.right)
                    continue
                elif d > depth:
                    return root
                queue.append((node.left, d + 1))
                queue.append((node.right, d + 1))
                
        return root

def main():
    s = Solution()

    r = s.addOneRow(deserialize('[4,2,6,3,1,5'), 1, 1)
    b = serialize(r)
    print(b)
    
    # print(serialize(s.addOneRow(deserialize('[4,2,6,3,1,5]'), 1, 2)))


if __name__ == '__main__':
    main()


"""
Runtime: 143 ms, faster than 5.00% of Python3 online submissions for Add One Row to Tree.
Memory Usage: 16.7 MB, less than 69.24% of Python3 online submissions for Add One Row to Tree.

oof

recursive

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1: return TreeNode(v, left=root) # edge case 
        
        def fn(node, d): 
            if d == 1: 
                node.left = TreeNode(v, left=node.left)
                node.right = TreeNode(v, right=node.right)
            if node.left: node.left = fn(node.left, d-1)
            if node.right: node.right = fn(node.right, d-1)
            return node 
        
        return fn(root, d-1)

and then there's this very clean level order traversal

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1: return TreeNode(v, left=root) # edge case 
        queue = [root]
        while queue: 
            d -= 1
            if d == 1: 
                for node in queue: 
                    node.left = TreeNode(v, left=node.left)
                    node.right = TreeNode(v, right=node.right)
                break 
            newq = []
            for node in queue: 
                if node.left: newq.append(node.left)
                if node.right: newq.append(node.right)
            queue = newq
        return root 
"""