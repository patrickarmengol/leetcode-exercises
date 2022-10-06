class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        for t in range(timestamp, 0, -1):
            v = self.m.get((key, t))
            if v:
                return v
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

def main():
    tm = TimeMap()
    tm.set('foo', 'bar', 1)
    print(tm.get('foo', 1))
    print(tm.get('foo', 3))
    tm.set('foo', 'bar2', 4)
    print(tm.get('foo', 4))
    print(tm.get('foo', 5))
    print(tm.get('foo', 2))

if __name__ == '__main__':
    main()

"""
Runtime: 758 ms, faster than 94.70% of Python3 online submissions for Time Based Key-Value Store.
Memory Usage: 77.3 MB, less than 6.40% of Python3 online submissions for Time Based Key-Value Store.

could use binary search to speed up get

class TimeMap:
    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]
"""