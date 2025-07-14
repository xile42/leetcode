class PhoneDirectory:

    def __init__(self, maxNumbers: int):

        self.valid = deque(range(maxNumbers))
        self.s = set()

    def get(self) -> int:

        if self.valid:
            v = self.valid.pop()
            self.s.add(v)
            return v

        return -1

    def check(self, number: int) -> bool:

        return number not in self.s

    def release(self, number: int) -> None:

        if number in self.s:
            self.s.remove(number)
            self.valid.append(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)