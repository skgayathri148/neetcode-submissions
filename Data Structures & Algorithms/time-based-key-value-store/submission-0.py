class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if len(self.time_map[key]) == 0:
            return ""
        
        val = ""
        l, r = 0, len(self.time_map[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.time_map[key][mid][1] == timestamp:
                return self.time_map[key][mid][0]
            elif self.time_map[key][mid][1] > timestamp:
                r = mid - 1
            else:
                val = self.time_map[key][mid][0]
                l = mid + 1

        return val
