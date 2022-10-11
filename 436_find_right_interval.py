def find_right_interval(intervals):
    def binary_search(l, x):
        lo = 0
        hi = len(l)
        while lo < hi:
            mid = (lo + hi) // 2
            if x > l[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo
    slist = sorted([(start, idx) for idx, (start, end) in enumerate(intervals)])
    results = []
    for start, end in intervals:
        bsi = binary_search(slist, (end,))
        if bsi == len(slist): # if binary search doesn't find eq or higher
            results.append(-1)
        else:
            results.append(slist[bsi][1])
    return results


def main():
    print(find_right_interval([(1, 2)]))
    print(find_right_interval([[3,4],[2,3],[1,2]]))
    print(find_right_interval([[1,4],[2,3],[3,4]]))


if __name__ == '__main__':
    main()


"""
could have used bisect.bisect_left() instead of writing my own binary search
"""