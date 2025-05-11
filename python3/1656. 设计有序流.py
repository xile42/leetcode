class OrderedStream:

    def __init__(self, n: int):
        self.d = dict()
        self.p = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.d[idKey] = value
        ans = list()
        while self.p in self.d:
            ans.append(self.d[self.p])
            self.p += 1

        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)