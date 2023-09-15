"""
neetcode - tries - 3

sol:
use a trie to store the words for lookup
dfs through board with a visited set
if cell is not valid, return
add to vis, reassign cur node, update word, if word end append to res
recurse on all neighbors
remove from vis
call dfs from each possible start
"""


class TrieNode:
    def __init__(self):
        self.end: bool = False
        self.children: dict[str, TrieNode] = dict()


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()

        # helper func for populating trie
        def addWord(root: TrieNode, word: str):
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.end = True

        # populate trie with all words
        for w in words:
            addWord(root, w)

        rows, cols = len(board), len(board[0])
        res: set[str] = set()
        vis: set[tuple[int, int]] = set()

        def dfs(r: int, c: int, node: TrieNode, word: str):
            if not (
                0 <= r < rows
                and 0 <= c < cols
                and (r, c) not in vis
                and board[r][c] in node.children
            ):
                return
            vis.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                res.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            vis.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)
