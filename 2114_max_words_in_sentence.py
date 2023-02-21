class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max([len(sen.split()) for sen in sentences])
