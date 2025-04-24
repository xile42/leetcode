class Checkout:

    def __init__(self):

        self.q = deque()
        self.l = deque()

    def get_max(self) -> int:

        return -1 if not self.q else self.q[0]

    def add(self, value: int) -> None:

        self.l.append(value)
        while self.q and self.q[-1] < value:
            self.q.pop()
        self.q.append(value)

    def remove(self) -> int:

        if not self.l:
            return -1
        v = self.l.popleft()
        if v == self.q[0]:
            self.q.popleft()

        return v
