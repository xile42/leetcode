class SmallestInfiniteSet:

    def __init__(self):

        self.h = list(range(1, 1000+1))
        heapify(self.h)

    def popSmallest(self) -> int:

        v = heappop(self.h)

        return v

    def addBack(self, num: int) -> None:

        if num not in set(self.h):
            heappush(self.h, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)