"""
neetcode - two pointers - 1

sol 1:
clean up the string
compare the list to its reverse

sol 2:
clean up the string
use two pointers to meet in the middle, comparing each char pair

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [c.lower() for c in s if c.isalnum()]
        return l == l[::-1]
