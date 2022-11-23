class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def int_to_ll(n):
    s = str(n)
    prev = head = ListNode(int(s[0]))
    for i in s[1:]:
        cur = ListNode(int(i))
        prev.next = cur
        prev = cur
    return head

def read_ll(head):
    cur = head
    s = ''
    while cur:
        s += str(cur.val)
        cur = cur.next
    return s

#test_head = int_to_ll(17898971)
#print(read_ll(test_head))


def is_palindrome(head):
    # pull the list into a string
    cur = head
    s = ''
    while cur:
        s += str(cur.val)
        cur = cur.next
    
    # use string slicing to compare
    midpoint = len(s) // 2
    left = s[:midpoint]
    right = s[-1:-1-midpoint:-1]
    return left == right


for test_head in [int_to_ll(i) for i in [1771, 333, 12345, 8282828, 12, 11, 1]]:
    print(is_palindrome(test_head))


"""
lol i totally forgot that i can do palindrome checking much more easily
s == s[::-1]

duh.....
"""