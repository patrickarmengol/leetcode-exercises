
def reverse_only_letters(s):
    r = []
    symbols = []
    for i, c in enumerate(s):
        if str.isalpha(c):
            r.append(c)
        else:
            symbols.append((i, c))
    r = r[::-1]
    for i, c in symbols:
        r.insert(i, c)
    return ''.join(r)


def main():
    print(reverse_only_letters('asdfqwe1r'))


if __name__ == '__main__':
    main()



"""
Runtime: 62 ms, faster than 20.65% of Python3 online submissions for Reverse Only Letters.
Memory Usage: 13.9 MB, less than 64.38% of Python3 online submissions for Reverse Only Letters.

seems my solution was pretty inefficient

this sol uses pointers at both ends of the list and reverses alpha chars it sees:
def reverseOnlyLetters(self, S):
    S, i, j = list(S), 0, len(S) - 1
    while i < j:
        if not S[i].isalpha():
            i += 1
        elif not S[j].isalpha():
            j -= 1
        else:
            S[i], S[j] = S[j], S[i]
            i, j = i + 1, j - 1
    return "".join(S)

this other one is a better version of my sol that uses a stack
def reverseOnlyLetters(self, S):
    stack = [x for x in S if x.isalpha()]
    return ''.join(stack.pop() if x.isalpha() else x for x in S)
"""