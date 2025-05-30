class Solution:

    def scheduleCourse(self, courses: List[List[int]]) -> int:

        h = list()
        ns = sorted(courses, key=lambda x: x[-1])

        cur_sum = 0
        for d, t in ns:
            if d > t:
                continue
            if not h:
                heappush(h, [-d, t])
                cur_sum = d
                continue
            if t - cur_sum >= d:
                heappush(h, [-d, t])
                cur = t
                cur_sum += d
                continue
            else:
                dd, tt = h[0]
                dd = -dd
                if dd > d and t - (cur_sum - dd) >= d:
                    heappop(h)
                    cur_sum += d - dd
                    heappush(h, [-d, t])

        return len(h)
