from os import times


class HitCounter:

    def __init__(self):

        self.t = list()

    def hit(self, timestamp: int) -> None:

        self.t.append(timestamp)

    def getHits(self, timestamp: int) -> int:

        while self.t and self.t[0] <= timestamp - 300:
            self.t.pop(0)

        return len(self.t)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)