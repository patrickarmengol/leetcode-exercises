def has_path_sum(root, target_sum):
    if not root:
        return False
    elif not root.left and not root.right:
        return (target_sum - root.val == 0)
    else:
        return has_path_sum(root.left, target_sum - root.val) or has_path_sum(root.right, target_sum - root.val)


"""
Runtime: 48 ms, faster than 88.77% of Python3 online submissions for Path Sum.
Memory Usage: 15.1 MB, less than 56.49% of Python3 online submissions for Path Sum.

recursive dfs
i kind of like my answer and i'm very glad i found it by myself
"""