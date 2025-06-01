class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        ans = 0
        intervals.sort(key=lambda x: x[0])

        s, e = intervals[0]
        for i in range(1, len(intervals)):
            ss, ee = intervals[i]
            if e <= ss:
                s, e = ss, ee
                continue
            ans += 1
            if e >= ee:
                s, e = ss, ee

        return ans
