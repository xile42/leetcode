class Solution:

    def findMinimumTime(self, strength: List[int], K: int) -> int:

        @cache
        def f(left, x):

            if not left:
                return 0

            ans = 0
            need = ceil(left[0] / x)
            while left and need == 1:
                left = left[1:]
                ans += 1
                x += K
                if not left:
                    break
                need = ceil(left[0] / x)

            min_ans = inf
            for idx, s in enumerate(left):
                min_ans = min(min_ans, f(tuple(left[:idx] + left[idx+1:]), x + K) + ceil(s / x))
            if min_ans != inf:
                ans += min_ans

            return ans

        ss = tuple(sorted(strength))
        ans = f(ss, 1)

        return ans

        # from bisect import bisect_right

        # ss = sorted(strength)
        # x = 1
        # ans = 0
        #
        # while len(ss):
        #
        #     need = ceil(ss[0] / x)
        #     while ss and need == 1:
        #         ss.pop(0)
        #         ans += 1
        #         x += K
        #         if not ss:
        #             break
        #         need = ceil(ss[0] / x)
        #
        #     if not ss:
        #         break
        #
        #     cur = need * x
        #     idx = bisect_right(ss, cur)
        #     ss.pop(idx - 1)
        #     ans += need
        #     x += K
        #
        # return ans
