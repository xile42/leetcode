class FirstUnique:

    def __init__(self, nums: List[int]):

        self.c = Counter(nums)
        self.ns = list()
        s = set()
        for v in nums:
            if v not in s:
                self.ns.append(v)
                s.add(v)

    def showFirstUnique(self) -> int:

        for v in self.ns:
            if self.c[v] == 1:
                return v

        return -1

    def add(self, value: int) -> None:

        if value not in self.c:
            self.ns.append(value)
        self.c[value] += 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)