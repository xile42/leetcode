class Solution:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) == 0:
            return True

        intervals = sorted(intervals, key=lambda x: x[0])
        cur = intervals[0][1]
        for s, e in intervals[1:]:
            if s < cur:
                return False
            cur = e

        return True
