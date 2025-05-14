class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:

        if 3 * limit < n:
            return 0

        # @cache
        # def g(i, cur):
        #
        #     if i >= 3:
        #         return 1 if cur == 0 else 0
        #
        #     ans = 0
        #     thres = (3 - i - 1) * limit
        #     for v in range(min(cur, limit) + 1):
        #         if cur - v > thres:
        #             continue
        #         ans += g(i + 1, cur - v)
        #
        #     return ans
        #
        # ans = g(0, n)
        #
        # return ans

        # 第一个熊孩子v1 [max(n - limit * 2, 0), min(limit, n)]
        # 第二个熊孩子v2 [max(n - v1 - limit, 0), min(limit, n - v1)]
        # 第三个熊孩子v3 n - v1 - v2

        ans = 0
        for v1 in range(max(n - limit * 2, 0), min(limit, n) + 1):
            ans += max(min(limit, n - v1) - max(n - v1 - limit, 0) + 1, 0)

        return ans
