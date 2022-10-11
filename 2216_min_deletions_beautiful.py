def min_deletion(nums):
    ndels = 0
    i = 0
    while i < len(nums) - 1:
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            del nums[i + 1]
            ndels += 1
        i += 2
    if len(nums) % 2 != 0:
        del nums[-1]
        ndels += 1
    return ndels


def main():
    print(min_deletion([1, 1, 2, 3, 5]))
    print(min_deletion([1, 1, 2, 2, 3, 3]))
    print(min_deletion([1]))
    print(min_deletion([]))
    print(min_deletion([0,1,5,4,2,4,7,2,3,0,3,0,0,9,7,5,9,4,3,9,9,2,1,6,3,1,0,7,6,6,6,0,1,7,1,9,4,9,3,3,4,5,0,3,8,7,1,8,4,5]))
    print(min_deletion([2,6,2,5,8,9,7,2,2,5,6,2,2,0,6,8,7,3,9,2,1,1,3,2,6,2,4,6,5,8,4,8,7,0,4,8,7,8,4,1,1,4,0,1,5,7,7,5,9,7,5,5,8,6,4,3,6,5,1,6,7,6,9,9,6,8,6,0,9,5,6,7,6,9,5,5,7,3,0,0,5,5,4,8,3,9,3,4,1,7,9,3,1,8,8,9,1,6,0,0]
))


if __name__ == '__main__':
    main()


"""
i shouldn't have modified the list, just count the num of deletions smartly
"""