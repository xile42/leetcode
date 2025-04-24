class CustomStack:

    def __init__(self, maxSize: int):

        self.st = list()
        self.size = maxSize

    def push(self, x: int) -> None:

        if len(self.st) == self.size:
            return

        self.st.append(x)

    def pop(self) -> int:

        if len(self.st) == 0:
            return -1

        return self.st.pop(-1)

    def increment(self, k: int, val: int) -> None:

        for i in range(min(k, len(self.st))):
            self.st[i] += val
