class Vector2D:

    def __init__(self, vec: List[List[int]]):

        self.ns = list() if len(vec) == 0 else reduce(add, vec)
        self.n = len(self.ns)
        self.i = 0

    def next(self) -> int:

        v = self.ns[self.i]
        self.i += 1

        return v

    def hasNext(self) -> bool:

        return False if self.n == 0 else True if self.i < self.n else False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()