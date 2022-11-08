def make_good(s: str) -> str:
    def same_letter(a: str, b: str) -> bool:
        return abs(ord(a) - ord(b)) == 32
    i = 0
    while i < len(s) - 1:
        if same_letter(s[i], s[i + 1]):
            s = s[:i] + s[i+2:]
            i = max((i - 1), 0)
        else:
            i += 1
    return s


def main() -> None:
    tests = [
        'leEeetcode',
        'abBAcC'
    ]
    for test in tests:
        print(make_good(test))

if __name__ == '__main__':
    main()


"""
i just iterated and backtracked 1 every match deletion

discussion had solution with stack:

def makeGood(self, s: str) -> str:
    stack = []
    for c in s:
        if stack and (abs(ord(stack[-1]) - ord(c))) == 32: stack.pop()
        else: stack.append(c)
    return "".join(stack)
"""