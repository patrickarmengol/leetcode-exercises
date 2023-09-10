"""
neetcode - trees - 15

can do recursive dfs for simplicity

sol: (level order emulating leetcode format)

"""
from __future__ import annotations
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        lr = []
        q = deque([root])

        while q:
            p = q.popleft()
            if p:
                q.append(p.left)
                q.append(p.right)
                lr.append(p.val)
            else:
                lr.append(None)

        # stringify
        while lr and lr[-1] is None:
            lr.pop()
        return f"[{','.join(str(i) for i in lr)}]".replace("None", "null")

    def deserialize(self, data: str) -> TreeNode | None:
        # parse the data into list
        ld = deque(int(e) if e.isdigit() else None for e in data.strip("[]").split(","))
        r = ld.popleft()
        root = TreeNode(r) if r is not None else None
        q = deque([root])

        while q:
            p = q.popleft()
            if not p:
                continue
            if ld:
                left_val = ld.popleft()
                p.left = TreeNode(left_val) if left_val is not None else None
                q.append(p.left)
            if ld:
                right_val = ld.popleft()
                p.right = TreeNode(right_val) if right_val is not None else None
                q.append(p.right)

        return root


ser = Codec()
deser = Codec()
root = deser.deserialize("[1,2,3,null,null,4,5]")
check = ser.serialize(root)
print(check)
ans = deser.deserialize(ser.serialize(root))
print(ans)
