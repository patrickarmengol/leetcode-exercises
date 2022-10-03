import random

def minimum_moves(s):
    moves = 0
    for i in range(len(s) - 2):
        #print(i)
        if s[i:i + 3] in ('XXX', 'XXO', 'XOX', 'XOO'):
            moves += 1
            s = s[:i] + 'OOO' + s[i + 3:]
        elif i == len(s) - 3 and 'X' in s[i:i + 3]:
            moves += 1
            s = s[:i] + 'OOO'
    return moves

def easier_minimum_moves(s):
    moves = 0
    i = 0
    while i < len(s):
        if s[i] == 'X':
            moves += 1
            i += 3
        else:
            i += 1
    return moves

def gen_random_strings(n):
    return [''.join([random.choice(('X', 'O')) for _ in range(20)]) for l in range(n)]

def main():
    test_strings = gen_random_strings(5)
    #print(test_strings)
    for t in test_strings:
        print(t)
        print(minimum_moves(t))

if __name__ == '__main__':
    main()

"""
Runtime: 102 ms, faster than 5.59% of Python3 online submissions for Minimum Moves to Convert String.
Memory Usage: 13.9 MB, less than 12.30% of Python3 online submissions for Minimum Moves to Convert String.

pretty darn slow
"""