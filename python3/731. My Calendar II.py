import bisect


class MyCalendarTwo:

    def __init__(self):

        self.intervals = list()

    def book(self, start: int, end: int) -> bool:

        if len(self.intervals) == 0:
            self.intervals.append((start, 1))
            self.intervals.append((end, -1))
            return True

        temp_intervals = self.intervals.copy()
        temp_intervals.append((start, 1))
        temp_intervals.append((end, -1))
        temp_intervals.sort()

        count = 0
        for _, value in temp_intervals:
            count += value
            if count >= 3:
                return False

        self.intervals = temp_intervals

        return True
