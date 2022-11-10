def remove_duplicates(s):
    stack = []
    for c in s:
        stack.append(c)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return ''.join(stack)


def main():
    tests = [
        'abbaca',
        'azxxzy'
    ]
    for test in tests:
        print(remove_duplicates(test))

if __name__ == '__main__':
    main()

"""
very similar to 1544
a nicer looking solution would be to check letters before pushing to stack

def remove_duplicates(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)
"""