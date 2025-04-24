class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = list()
        

    def push(self, x: int) -> None:

        if not len(self.st):
            self.st.append([x, x])
        else:
            cur = self.st[-1][-1]
            self.st.append([x, min(x, cur)])

    def pop(self) -> None:

        self.st.pop(-1)

    def top(self) -> int:

        return self.st[-1][0]
        

    def getMin(self) -> int:

        return self.st[-1][-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
