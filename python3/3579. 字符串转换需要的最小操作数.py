def mn(a, b):
    return a if a < b else b


class Solution:

    def minOperations(self, s1: str, s2: str) -> int:

        # @cache
        # def f(i, j):  # [i:j] 的最小操作次数
        #
        #     ans = inf
        #     for k in range(i + 1, j):
        #         ans = mn(ans, f(i, k) + f(k, j))
        #         # print("f({}, {})遍历中".format(i, j), s1[i:k], s2[i:k], f(i, k), s1[k:j], s2[k:j], f(k, j), f(i, k) + f(k, j))
        #     # print("f({}, {})遍历后".format(i, j), s1[i:j], s2[i:j], ans)
        #
        #     # 逐个替换
        #     sub_ans = 0
        #     ss1 = s1[i:j]
        #     ss2 = s2[i:j]
        #     vis = [False] * len(ss1)
        #     for idx, (c1, c2) in enumerate(zip(ss1, ss2)):
        #         if vis[idx]:
        #             continue
        #         if c1 != c2:
        #             for jdx in range(idx + 1, len(ss1)):
        #                 if c1 != ss1[jdx] and c1 == ss2[jdx] and ss1[jdx] == ss2[idx]:
        #                     # print(s1[i:j], s2[i:j], idx, jdx, "matched")
        #                     vis[jdx] = True
        #                     sub_ans += 1
        #                     break
        #             else:
        #                 sub_ans += 1
        #     # print("逐个替换", ss1, ss2, sub_ans)
        #     ans = mn(ans, sub_ans)
        #
        #     # 反转后逐个替换
        #     sub_ans = 1  # 反转
        #     ss1 = s1[i:j][::-1]
        #     ss2 = s2[i:j]
        #     vis = [False] * len(ss1)
        #     for idx, (c1, c2) in enumerate(zip(ss1, ss2)):
        #         if vis[idx]:
        #             continue
        #         if c1 != c2:
        #             for jdx in range(idx + 1, len(ss1)):
        #                 if c1 != ss1[jdx] and c1 == ss2[jdx] and ss1[jdx] == ss2[idx]:
        #                     vis[jdx] = True
        #                     sub_ans += 1
        #                     break
        #             else:
        #                 sub_ans += 1
        #     # print("反转后逐个替换", ss1, ss2, sub_ans)
        #     ans = mn(ans, sub_ans)
        #
        #
        #     print("返回", s1[i:j], s2[i:j], ans)
        #     return ans
        #
        # ans = f(0, len(s1))
        # f.cache_clear()
        #
        # return ans

        n = len(s1)

        dp = [[inf] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][i] = 0
        for i in range(n):
            dp[i][i + 1] = 0 if s1[i] == s2[i] else 1

        def calc(s, t):

            ns = len(s)
            diff_cnt = 0
            cnt = defaultdict(int)
            for i in range(ns):
                if s[i] != t[i]:
                    diff_cnt += 1
                    cnt[(s[i], t[i])] += 1
            swap = 0

            for key in list(cnt.keys()):
                a, b = key
                if a < b:
                    key2 = (b, a)
                    swap += min(cnt[key], cnt.get(key2, 0))

            return diff_cnt - swap

        for l in range(2, n + 1):
            for i in range(0, n - l + 1):
                j = i + l

                for k in range(i + 1, j):
                    dp[i][j] = mn(dp[i][j], dp[i][k] + dp[k][j])

                ss1 = s1[i:j]
                ss2 = s2[i:j]

                op1 = calc(ss1, ss2)
                op2 = 1 + calc(ss1[::-1], ss2)

                dp[i][j] = mn(dp[i][j], mn(op1, op2))

        return dp[0][n]
