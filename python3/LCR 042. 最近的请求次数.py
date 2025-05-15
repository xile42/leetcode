class RecentCounter:

    def __init__(self):

        self.ns = list()

    def ping(self, t: int) -> int:

        self.ns.append(t)
        idx = 0
        while self.ns[idx] < t - 3000:
            idx += 1
        self.ns = self.ns[idx:]

        return len(self.ns)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)