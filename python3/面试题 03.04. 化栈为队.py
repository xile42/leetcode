class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = list()
        self.b = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.a.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.a:
            self.b.append(self.a.pop(-1))
        v = self.b.pop(-1)
        while self.b:
            self.a.append(self.b.pop(-1))

        return v

    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.a:
            self.b.append(self.a.pop(-1))
        v = self.b[-1]
        while self.b:
            self.a.append(self.b.pop(-1))

        return v

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.a) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()