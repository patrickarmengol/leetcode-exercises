
def arrange_words(text: str) -> str:
    words = text.split(' ')
    swords = sorted(words, key=len)
    return ' '.join(swords).capitalize()


def main():
    tests = (
        'Leetcode is cool',
        'Keep calm and code on',
        'To be or not to be'
    )
    for test in tests:
        print(arrange_words(test))

if __name__ == '__main__':
    main()