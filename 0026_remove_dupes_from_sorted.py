def remove_duplicates(nums):
    i = 0
    prev = 101
    while i < len(nums):
        if nums[i] == prev:
            del nums[i]
        else:
            prev = nums[i]
            i += 1
    return len(nums)

def main():
    tests = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ]
    for test in tests:
        print(remove_duplicates(test))

if __name__ == '__main__':
    main()