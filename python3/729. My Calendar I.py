import bisect


class MyCalendar:

    def __init__(self):

        self.booked = list()

    def book(self, start: int, end: int) -> bool:

        index_1 = bisect.bisect_right(self.booked, start)
        index_2 = bisect.bisect_left(self.booked, end)
        if index_1 != index_2 or index_1 % 2 == 1:
            return False
        self.booked.insert(index_1, end)
        self.booked.insert(index_1, start)

        return True
