class FrontMiddleBackQueue:

    def __init__(self):

        self.q1 = deque()
        self.q2 = deque()

    def pushFront(self, val: int) -> None:

        self.q1.appendleft(val)
        while len(self.q1) > len(self.q2):
            self.q2.appendleft(self.q1.pop())

    def pushMiddle(self, val: int) -> None:

        if len(self.q1) < len(self.q2):
            self.q1.append(val)
        else:
            self.q2.appendleft(val)

    def pushBack(self, val: int) -> None:

        self.q2.append(val)
        while len(self.q2) > len(self.q1) + 1:
            self.q1.append(self.q2.popleft())

    def popFront(self) -> int:

        if len(self.q1) + len(self.q2) == 0:
            return -1

        if self.q1:
            val = self.q1.popleft()
        else:
            val = self.q2.popleft()

        while len(self.q2) > len(self.q1) + 1:
            self.q1.append(self.q2.popleft())

        return val

    def popMiddle(self) -> int:

        if len(self.q1) + len(self.q2) == 0:
            return -1

        if len(self.q1) < len(self.q2):
            val = self.q2.popleft()
        else:
            val = self.q1.pop()

        return val

    def popBack(self) -> int:

        if len(self.q1) + len(self.q2) == 0:
            return -1

        val = self.q2.pop()

        while len(self.q2) < len(self.q1):
            self.q2.appendleft(self.q1.pop())

        return val

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()