class ZigzagIterator:

    def __init__(self, v1: List[int], v2: List[int]):

        self.v1 = v1
        self.v2 = v2
        self.flag = 0

    def next(self) -> int:

        ans = (self.v1.pop(0) if self.v1 else self.v2.pop(0)) if not self.flag else (self.v2.pop(0) if self.v2 else self.v1.pop(0))
        self.flag = 1 - self.flag

        return ans

    def hasNext(self) -> bool:

        return len(self.v1) > 0 or len(self.v2) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())