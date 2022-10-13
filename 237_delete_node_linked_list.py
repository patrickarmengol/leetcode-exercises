class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_node(node : ListNode):
    node.val = node.next.val
    node.next = node.next.next

"""
why was this problem labeled medium difficulty?
"""