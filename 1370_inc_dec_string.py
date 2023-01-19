from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        res: list[str] = []
        counter = Counter(s)
        while len(res) < len(s):
            letters = sorted(k for k, v in counter.items() if v != 0)
            for letter in letters + letters[::-1]:
                if counter[letter] > 0:
                    counter[letter] -= 1
                    res.append(letter)
        return ''.join(res)
