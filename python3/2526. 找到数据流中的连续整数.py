class DataStream:

    def __init__(self, value: int, k: int):

        self.ns = list()
        self.c = Counter()
        self.k = k
        self.value = value

    def consec(self, num: int) -> bool:

        self.ns.append(num)
        self.c[num] += 1
        if len(self.ns) > self.k:
            self.c[self.ns.pop(0)] -= 1

        return self.c[self.value] == self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)