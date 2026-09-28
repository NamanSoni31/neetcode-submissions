class TimeMap:
    d = {}
    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d: 
            self.d[key].append([value, timestamp])
        else: 
            self.d[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d: 
            l = 0
            r = len(self.d[key]) - 1
            lowerVal = -1
            while l <= r:
                mid = (l+r) // 2
                time = int(self.d[key][mid][1])
                if self.d[key][mid][1] == timestamp: 
                    return self.d[key][mid][0]
                elif time < timestamp:
                    l = mid + 1
                    if(time > lowerVal):
                        lowerVal = mid
                else: 
                    r = mid - 1
            if lowerVal == -1: 
                return ''
            return self.d[key][lowerVal][0]
        if key not in self.d:
            return ''