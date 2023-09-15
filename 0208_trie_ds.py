"""
neetcode - tries - 1

a trie is a k-ary tree

sol:
declare a trienode that has children and an end marker
to insert:
    - node point to root
    - iterate through characters in word
    - if c not in cur node's children, add to children
    - update node to child
    - once reach end, set node's end bool to true
to search:
    - node point to root
    - iterate through characters in word
    - if c in children, set node to child
    - else return false
    - once reach end return whether node marked as end
to check prefix:
    - node point to root
    - iterate through characters in prefix
    - if c in children, set node to child
    - else return false
    - once reach end return true
"""

from __future__ import annotations


class TrieNode:
    def __init__(self, letter: str, end: bool, children: dict[str, TrieNode]):
        self.letter = letter
        self.end = end
        self.children = children


class Trie:
    def __init__(self):
        self.root = TrieNode("", False, dict())

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c, False, dict())
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True


t = Trie()
print(t.startsWith("a"))
