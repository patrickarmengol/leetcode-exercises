def array_strings_are_equal(words1, words2):
    return ''.join(words1) == ''.join(words2)


def main():
    print(array_strings_are_equal(['ab', 'c'], ['a', 'bc']))
    print(array_strings_are_equal(["abc", "d", "defg"], ["abcddefg"]))

if __name__ == '__main__':
    main()


"""
apparently my approach is naive

the better answer is:
use generators that iterate through each word in the wordlists, each char in word
compare each char; if mismatch return False
this exits early on rather than building strings for each list and comparing full strings


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.generate(word1), self.generate(word2)):
            if c1 != c2:
                return False
        return True

    def generate(self, wordlist: List[str]):
        for word in wordlist:
            for char in word:
                yield char
        yield None

"""