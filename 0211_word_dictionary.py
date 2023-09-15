"""
neetcode - tries - 2
"""
from __future__ import annotations


class TrieNode:
    def __init__(self, end: bool, children: dict[str, TrieNode]):
        self.end = end
        self.children = children


class WordDictionary:
    def __init__(self):
        self.root = TrieNode(False, dict())

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(False, dict())
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        # recursive dfs
        def dfs(j, root) -> bool:
            node = root
            # iterate from end of last recurse onward
            for i in range(j, len(word)):
                c = word[i]
                # case is .
                if c == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                # case not .
                else:
                    # update child
                    if c in node.children:
                        node = node.children[c]
                    # next char not in path
                    else:
                        return False
            # reached end; check if complete word
            return node.end

        return dfs(0, self.root)
