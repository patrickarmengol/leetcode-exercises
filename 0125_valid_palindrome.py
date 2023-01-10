class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [c.lower() for c in s if c.isalnum()]
        return l == l[::-1]


"""
could also use two pointers comparing at each pair of alnum chars
"""
