class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.ns = list()
        self.size = size
        self.s = 0

    def next(self, val: int) -> float:

        self.ns.append(val)
        self.s += val
        if len(self.ns) > self.size:
            self.s -= self.ns.pop(0)

        return self.s / len(self.ns)
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
