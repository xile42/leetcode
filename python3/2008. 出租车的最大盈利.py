class Solution:

    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:

        rides.sort(key=lambda x: x[0])
        ns = [i[0] for i in rides]

        @cache
        def f(i):

            if i >= len(rides):
                return 0

            next_start = rides[i][1]
            next_i = bisect_left(ns, next_start)

            ans1 = rides[i][1] - rides[i][0] + rides[i][2] + f(next_i)
            ans2 = f(i + 1)

            return max(ans1, ans2)

        ans = f(0)
        f.cache_clear()

        return ans
