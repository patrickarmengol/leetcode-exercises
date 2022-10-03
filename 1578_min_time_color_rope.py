def min_cost(colors, needed_time):
    import heapq
    minheap = []
    time_cost = 0
    prev_c = ''
    start = 0
    end = 0
    for i, c in enumerate(colors):
        # if streak found, increment end pointer
        if c == prev_c:
            end = i
        # if streak is broken or we reached the end of the list, remove balloons as needed
        if c != prev_c or i == len(colors) - 1:
            if end > start:
                # add all elements of streak to minheap
                for j in range(start, end + 1):
                    heapq.heappush(minheap, (needed_time[j], j))
                # pop all but one out, accumulating their cost
                while len(minheap) > 1:
                    to_remove = heapq.heappop(minheap)
                    time_cost += to_remove[0]
                minheap = []
            start = i
        prev_c = c
    return time_cost




def main():
    print(min_cost("abaac", [1,2,3,4,5]))
    print(min_cost("abc", [1,2,3]))
    print(min_cost("aabaa", [1,2,3,4,1]))

if __name__ == '__main__':
    main()


"""
minheap not really needed
some other solutions that I thought were good:


def minCost(self, colors: str, neededTime: List[int]) -> int:
    sameColorsTime = [neededTime[0]]
    totalTime = 0
    for i in range(1, len(colors)):
        if colors[i-1] == colors[i]:
            sameColorsTime.append(neededTime[i])
        else:
            totalTime += sum(sameColorsTime) - max(sameColorsTime)
            sameColorsTime = [neededTime[i]]
    
    totalTime += sum(sameColorsTime) - max(sameColorsTime)
    return totalTime


keep track of a max value within a streak, reset to 0 when streak breaks

def minCost(self, s, cost):
    res = max_cost = 0
    for i in range(len(s)):
        if i > 0 and s[i] != s[i - 1]:
            max_cost = 0
        res += min(max_cost, cost[i])
        max_cost = max(max_cost, cost[i])
    return res
"""