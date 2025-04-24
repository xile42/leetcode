class TripleInOne:

    def __init__(self, stackSize: int):

        self.stackSize = stackSize
        self.st = [0] * (stackSize * 3)
        self.start = [0, self.stackSize, self.stackSize * 2]
        self.empty = [0, self.stackSize, self.stackSize * 2]
        self.full = [self.stackSize, self.stackSize * 2, self.stackSize * 3]

    def push(self, stackNum: int, value: int) -> None:

        if self.start[stackNum] == self.full[stackNum]:
            return
        self.st[self.start[stackNum]] = value
        self.start[stackNum] += 1

    def pop(self, stackNum: int) -> int:

        if self.start[stackNum] == self.empty[stackNum]:
            return -1
        self.start[stackNum] -= 1
        return self.st[self.start[stackNum]]

    def peek(self, stackNum: int) -> int:
        
        if self.start[stackNum] == self.empty[stackNum]:
            return -1
        return self.st[self.start[stackNum] - 1]

    def isEmpty(self, stackNum: int) -> bool:
        
        return self.start[stackNum] == self.empty[stackNum]
