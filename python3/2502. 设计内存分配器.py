class Allocator:

    def __init__(self, n: int):
        self.ns = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        cur = 0
        for i, ite in groupby(self.ns):
            l = len(list(ite))
            if i == 0 and l >= size:
                self.ns[cur:cur + size] = [mID] * size
                return cur
            else:
                cur += l

        return -1

    def freeMemory(self, mID: int) -> int:

        cnt = 0
        for i, v in enumerate(self.ns):
            if v == mID:
                cnt += 1
                self.ns[i] = 0

        return cnt

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)