# 有一组 n 个人作为实验对象，从 0 到 n - 1 编号，其中每个人都有不同数目的钱，以及不同程度的安静值（quietness）。为了方便起见，我们将编号为 x 的人简称为 "person x "。
#
# 给你一个数组 richer ，其中 richer[i] = [ai, bi] 表示 person ai 比 person bi 更有钱。另给你一个整数数组 quiet ，其中 quiet[i] 是 person i 的安静值。richer 中所给出的数据 逻辑自洽（也就是说，在 person x 比 person y 更有钱的同时，不会出现 person y 比 person x 更有钱的情况 ）。
#
# 现在，返回一个整数数组 answer 作为答案，其中 answer[x] = y 的前提是，在所有拥有的钱肯定不少于 person x 的人中，person y 是最不安静的人（也就是安静值 quiet[y] 最小的人）。
#


class Solution:

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        n = len(quiet)
        g = defaultdict(list)
        for a, b in richer:
            g[b].append(a)

        def f(i):

            nonlocal mn, mn_idx
            vis[i] = True
            v = quiet[i]
            if v < mn:
                mn = v
                mn_idx = i
            for j in g[i]:
                if vis[j]:
                    continue
                f(j)

        ans = list()
        for i in range(n):
            vis = [False] * n
            mn = quiet[i]
            mn_idx = i
            f(i)
            ans.append(mn_idx)

        return ans
