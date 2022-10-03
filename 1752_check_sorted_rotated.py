def check_sorted_rotated(nums):
    sorted_nums = sorted(nums)
    split_idx = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            split_idx = i
            break
    test_nums = nums[split_idx:] + nums[:split_idx]
    return test_nums == sorted_nums


# max 1 case where n[i] < n[i-1]
# also checks edge of list n[0] < n[0-1]
def way_better_check_sorted_rotated(nums):
    return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1 


def main():
    print(check_sorted_rotated([3, 4, 5, 1, 2]))
    print(check_sorted_rotated([2, 1, 3, 4]))
    print(check_sorted_rotated([1, 2, 3]))

if __name__ == '__main__':
    main()
