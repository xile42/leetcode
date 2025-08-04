class MedianFinder:

    def __init__(self):

        self.s = SortedList()

    def addNum(self, num: int) -> None:

        self.s.add(num)

    def findMedian(self) -> float:

        l = len(self.s)
        if l & 1:
            return self.s[l // 2]
        else:
            return (self.s[l // 2 - 1] + self.s[l // 2]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()