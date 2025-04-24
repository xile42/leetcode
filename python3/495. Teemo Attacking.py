class Solution:

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        timeSeries = sorted(set(timeSeries))

        intervals = list()
        for t in timeSeries:
            intervals.append([t, t+duration-1])

        merged = list()
        merged.append(intervals[0])

        for interval in intervals[1:]:
            start, end = merged[-1]
            _start, _end = interval
            if _start <= end:
                merged.pop(-1)
                merged.append([start, _end])
            else:
                merged.append([_start, _end])

        return sum([i[1] - i[0] + 1 for i in merged])
