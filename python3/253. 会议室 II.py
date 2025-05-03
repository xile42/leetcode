class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        ns = list()
        for s, e in intervals:
            ns.append([s, 1])
            ns.append([e, 0])

        ns.sort()
        ans = 0
        cur = 0
        for _, k in ns:
            cur += -1 if k == 0 else 1
            ans = max(ans, cur)

        return ans