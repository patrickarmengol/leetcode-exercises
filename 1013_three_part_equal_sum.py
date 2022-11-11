def can_three_parts_equal_sum(arr):
    s = sum(arr)
    if s % 3:
        return False
    d3 = s // 3
    i = 0
    left = 0
    j = len(arr) - 1
    right = 0
    mid = s
    while (left != d3 or right != d3 or mid != d3) or (i == 0 and j == len(arr) - 1):
        if i == 0 or left != d3:
            left += arr[i]
            i += 1
        if j == len(arr) - 1 or right != d3:
            right += arr[j]
            j -= 1
        mid = s - left - right
        if i > j:
            return False
    return True

def main():
    tests = [
        [0,2,1,-6,6,-7,9,1,2,0,1],
        [0,2,1,-6,6,7,9,-1,2,0,1],
        [3,3,6,5,-2,2,5,1,-9,4],
        [1,-1,1,-1],
        [18,12,-18,18,-19,-1,10,10]
    ]
    for test in tests:
        print(can_three_parts_equal_sum(test))

if __name__ == '__main__':
    main()


"""
what a mess
i should have iterated from left, accumulating and checking if matches d3 and resetting
then check that i reached d3 3 times
"""