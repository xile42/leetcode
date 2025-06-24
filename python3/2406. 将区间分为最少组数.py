class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        h = list()

        for s, e in intervals:
            if not h:
                heappush(h, e)
            elif h[0] < s:
                heappop(h)
                heappush(h, e)
            else:
                heappush(h, e)

        return len(h)
