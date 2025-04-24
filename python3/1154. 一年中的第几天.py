from datetime import datetime


class Solution:

    def dayOfYear(self, date: str) -> int:

        t1 = datetime.strptime(date, "%Y-%m-%d")
        t2 = datetime.strptime(date[:4]+"-01-01", "%Y-%m-%d")

        return (t1 - t2).days + 1
