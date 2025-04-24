class TwoSum:

    def __init__(self):

        self.s = set()
        self.c = Counter()
        

    def add(self, number: int) -> None:

        self.s.add(number)
        self.c[number] += 1
        

    def find(self, value: int) -> bool:

        for n in self.s:
            if value - n in self.s and (n != value - n or slef.c[n] > 1):
                return True

        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
