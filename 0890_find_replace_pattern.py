class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        res: list[str] = []
        pletters = list(dict.fromkeys(pattern))
        for word in words:
            orig = word
            wletters = list(dict.fromkeys(word))
            if len(wletters) != len(pletters):
                continue
            m: dict[str, str] = dict(zip(wletters, pletters))
            word = ''.join(m[letter] for letter in word)
            # print(f'{word =} {pattern =}')
            if word == pattern:
                res.append(orig)
        return res


"""
definitely overcomplicated this one

sol with two maps
def findAndReplacePattern(self, words, p):
        def match(w):
            m1, m2 = {}, {}
            return all((m1.setdefault(i, j), m2.setdefault(j, i)) == (j, i) for i, j in zip(w, p))
        return filter(match, words)

sol with numeric pattern
def findAndReplacePattern(self, words: List[str], p: str) -> List[str]:
    def find(w): # function thats calculate the numeric pattern
        l = []
        m = defaultdict(int)
        i = 0
        for c in w:
            if c in m:
                l.append(m[c])
            else:
                i+=1
                m[c]=i
                l.append(m[c])
        return l
    ans = []
    pfind = find(p)
    for w in words:
        wfind = find(w)
        if wfind == pfind: ans.append(w) #check if numeric pattern of pattern is equal to pattern of word 
    return ans
"""
