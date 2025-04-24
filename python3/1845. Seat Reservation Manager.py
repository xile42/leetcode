import bisect


class SeatManager:

    def __init__(self, n: int):

        self.valid = list(range(1, n+1))

    def reserve(self) -> int:

        idx = self.valid.pop(0)
        return idx

    def unreserve(self, seatNumber: int) -> None:

        idx = bisect.bisect_right(self.valid, seatNumber)
        self.valid.insert(idx, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)