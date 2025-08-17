class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        cnt = 0
        cur_start, cur_end = intervals[0]
        for start, end in intervals[1:]:
            if end <= cur_end:
                cnt += 1
            else:
                cur_end = max(cur_end, end)

        return len(intervals) - cnt
