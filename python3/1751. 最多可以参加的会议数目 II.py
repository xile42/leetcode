fmax = lambda x, y: x if x > y else y


class Solution:

    def maxValue(self, events: List[List[int]], k: int) -> int:

        n = len(events)
        events.sort(key=lambda x: x[0])
        starts = [i[0] for i in events]

        @cache
        def f(i, left):

            if i >= n or left == 0:
                return 0

            ans = f(i + 1, left)

            # 这样能过
            s, e, v = events[i]
            ii = bisect_right(starts, e, lo=i + 1)
            ans = fmax(ans, v + f(ii, left - 1))

            # # 这样过不了
            # for j in range(i, n):
            #     s, e, v = events[j]
            #     ii = bisect_right(starts, e, lo=j + 1)
            #     ans = fmax(ans, v + f(ii, left - 1))

            return ans

        return f(0, k)
