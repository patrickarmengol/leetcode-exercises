"""
neetcode - binary search - 6

sol:
use multiple defaultdicts of lists
one for appending data at particular key
other for appending timestamps at particular key
since time is linear, timestamps always sorted; can use binary search on timestamp list

could use one map with tuples of (value, timestamp), but this is cleaner
"""

from collections import defaultdict
import bisect


class TimeMap:
    def __init__(self):
        self.times = defaultdict(list)
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.times[key], timestamp)
        if idx == 0:
            return ""
        return self.data[key][idx - 1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


def main():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))
    print(tm.get("foo", 3))
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))
    print(tm.get("foo", 5))
    print(tm.get("foo", 2))


if __name__ == "__main__":
    main()
