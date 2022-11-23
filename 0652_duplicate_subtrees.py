import collections

# Definition for a binary tree node.
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

def find_duplicate_subtrees(root):
    # bfs through tree
    # add serialized sub to dictionary

    dupes = []
    dupset = set()
    d = {}
    queue = collections.deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node:
            ns = serialize(node)
            if ns in d and ns not in dupset:
                dupes.append(node)
                dupset.add(ns)
            else:
                d[ns] = True
            queue.append(node.left)
            queue.append(node.right)
    
    return dupes


# going to try recursion and simple serialization

def alt_find(root):
    subtrees = collections.defaultdict(list)
    def walk_tree(node):
        if node:
            tree_ser = f'{node.val} {walk_tree(node.left)} {walk_tree(node.right)}'
            subtrees[tree_ser].append(node)
            return tree_ser
        else:
            return 'null'
    walk_tree(root)
    return [trees[0] for trees in subtrees.values() if len(trees) > 1]


def main():
    tests = [
        '[1,2,3,4,null,2,4,null,null,4]',
        '[2,1,1]',
        '[2,2,2,3,null,3,null]'
    ]
    for test in tests:
        test_root = deserialize(test)
        #dupes = find_duplicate_subtrees(test_root)
        dupes = alt_find(test_root)
        print('result')
        for dupe in dupes:
            print(serialize(dupe))
        print()

if __name__ == '__main__':
    main()