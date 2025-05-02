class Solution:

    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:

        ans = 1
        g1 = defaultdict(list)
        g2 = defaultdict(list)
        for i, (s, e) in enumerate(pairs1):
            g1[s].append([e, rates1[i]])
            g1[e].append([s, 1 / rates1[i]])
        for i, (s, e) in enumerate(pairs2):
            g2[s].append([e, rates2[i]])
            g2[e].append([s, 1 / rates2[i]])
        currencies = set([initialCurrency] + reduce(add, pairs1) + reduce(add, pairs2))
        vis_all = {k: False for k in currencies}

        def dfs(cur, vis, amt, day):

            nonlocal ans

            if day == 3:
                if cur == initialCurrency:
                    ans = max(ans, amt)
                return

            vis[cur] = True
            g = g1 if day == 1 else g2

            for next, rate in g[cur]:
                if vis[next]:
                    continue
                dfs(next, vis, amt * rate, day)

            dfs(cur, vis_all.copy(), amt, day + 1)

        dfs(initialCurrency, vis_all.copy(), 1, 1)

        return ans
