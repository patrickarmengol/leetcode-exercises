import functools

def largest_number(nums):
    def sorted_by(a, b):
        if a == b:
            return 0
        elif a + b < b + a: # a->b is smaller than b->a; a is sorted lower
            return -1
        else:
            return 1
    return ''.join(sorted([str(n) for n in nums], reverse=True, key=functools.cmp_to_key(sorted_by))).lstrip('0') or '0'


def main():
    print(largest_number([3, 30, 34, 5, 9]))
    print(largest_number([111311, 1113]))

if __name__ == '__main__':
    main()




"""
Runtime: 31 ms, faster than 99.57% of Python3 online submissions for Largest Number.
Memory Usage: 13.9 MB, less than 67.64% of Python3 online submissions for Largest Number.

i really didn't want to write my own sort, so i did everything i could use python's sorted()
i initially failed on edge cases [0, 0] and [0], which was annoying
"""