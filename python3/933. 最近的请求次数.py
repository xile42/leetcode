class RecentCounter:

    def __init__(self):

        self.ts = list()
        

    def ping(self, t: int) -> int:

        while self.ts and self.ts[0] < t - 3000:
            self.ts.pop(0)

        self.ts.append(t)

        return len(self.ts)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
