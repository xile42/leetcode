from datetime import datetime


class Solution:

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        s1, e1 = datetime.strptime(arriveAlice, "%m-%d"), datetime.strptime(leaveAlice, "%m-%d")
        s2, e2 = datetime.strptime(arriveBob, "%m-%d"), datetime.strptime(leaveBob, "%m-%d")

        if s2 > e1 or s1 > e2:
            return 0

        return (min(e2, e1) - max(s1, s2)).days + 1
