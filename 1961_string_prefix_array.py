

def is_prefix_string(s, words):
    ws = ''
    while len(ws) < len(s) and words:
        ws += words.pop(0)
    return s == ws


def main():
    print(is_prefix_string('iloveleetcode', ['i', 'love', 'leet', 'code', 'apples']))
    print(is_prefix_string('iloveleetcode', ['i', 'love', 'apples', 'leet', 'code', 'apples']))

if __name__ == '__main__':
    main()


"""
Runtime: 50 ms, faster than 70.44% of Python3 online submissions for Check If String Is a Prefix of Array.
Memory Usage: 13.9 MB, less than 66.82% of Python3 online submissions for Check If String Is a Prefix of Array.

meh
"""