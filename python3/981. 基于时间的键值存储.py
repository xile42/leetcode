class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.dict[key]:
            return ""
        if self.dict[key][0][0] > timestamp:
            return ""
        if self.dict[key][-1][0] <= timestamp:
            return self.dict[key][-1][1]
        l,r = 0,len(self.dict[key]) -1 
        while l <= r:
            mid = l+(r-l)//2
            if self.dict[key][mid][0] < timestamp+1:
                l += 1
            else:
                r -= 1
        return self.dict[key][-1][1] if l == len(self.dict[key]) else self.dict[key][l-1][1]
