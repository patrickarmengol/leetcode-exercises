def find_final_value(nums, original):
    snums = sorted(nums)
    for n in snums:
        if original < n:
            break
        elif original == n:
            original *= 2
    return original

def main():
    tests = [
        ([5, 3, 6, 1, 12], 3),
        ([2, 7, 9], 4)
    ]
    for test in tests:
        print(find_final_value(*test))

if __name__ == '__main__':
    main()


"""
maybe better solution is to check for membership in a set or hashtable

def find_final_value(nums, original):
    snums = set(nums)
    while original in snums:
        original += 2
    return original
"""