class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = list()


    def push(self, x: int) -> None:

        if len(self.st):
            self.st.append([x, min(x, self.st[-1][-1])])
        else:
            self.st.append([x, x])

    def pop(self) -> None:

        return self.st.pop(-1)[0]

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
