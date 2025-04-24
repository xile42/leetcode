class CQueue:

    def __init__(self):

        self.st = list()
        

    def appendTail(self, value: int) -> None:

        self.st.append(value)


    def deleteHead(self) -> int:

        return -1 if not len(self.st) else self.st.pop(0)


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
