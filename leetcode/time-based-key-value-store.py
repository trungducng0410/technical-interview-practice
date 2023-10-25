# Brute force solution
from collections import defaultdict


class TimeMap:
    # O(1)
    def __init__(self):
        self.timeMap = defaultdict(list)

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    # O(n)
    def get(self, key: str, timestamp: int) -> str:
        # This array is always increasing, so we can optimize the search using binary search
        values = self.timeMap[key]

        if len(values) == 0:
            return ""

        res = ""
        for value in values:
            if value[1] == timestamp:
                return value[0]
            elif value[1] <= timestamp:
                res = value[0]

        return res


# Optimal solution using binary search
class TimeMap:

    # O(1)
    def __init__(self):
        self.timeMap = defaultdict(list)

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    # O(logn)
    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]

        if len(values) == 0:
            return ""

        res = ""
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2

            midValue, midTimestamp = values[mid]
            if midTimestamp <= timestamp:
                res = midValue
                left = mid + 1
            else:
                right = mid - 1

        return res
