class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:

        h = list()
        idx = 0
        events = sorted(events, key=lambda x: x[0])

        ans = 0
        for cur in range(1, max([i[1] for i in events]) + 1):
            while idx < len(events) and events[idx][0] <= cur:
                heappush(h, events[idx][1])
                idx += 1
            while h and h[0] < cur:
                heappop(h)
            if h:
                heappop(h)
                ans += 1

        return ans
