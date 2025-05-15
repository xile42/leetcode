class Solution:

    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:

        # g = [[] for _ in range(n)]
        # for x, y, w in edges:
        #     g[x].append((y, w))
        #
        # ans = -1
        # vis = [False] * n
        #
        # def dfs(x, fa, path, cur_sum):
        #
        #     vis[x] = True
        #     # print("IN f({}, {}, {}, {})".format(x, fa, path, cur_sum))
        #     nonlocal ans
        #     if len(path) == k:
        #         if cur_sum < t:
        #             # print("UPDATE f({}, {}, {}, {})".format(x, fa, path, cur_sum))
        #             ans = max(ans, cur_sum)
        #
        #     for y, w in g[x]:
        #         if y != fa:
        #             if len(path) == k:
        #                 dfs(y, x, path[1:] + [w], cur_sum + w - (0 if not path else path[0]))
        #             else:
        #                 dfs(y, x, path + [w], cur_sum + w)
        #
        # for i in range(n):
        #     if not vis[i]:
        #         dfs(i, -1, [], 0)
        #
        # return ans

        if k == 0:
            return 0 if t > 0 else -1

        dp = [{} for _ in range(k + 1)]
        for u in range(n):
            dp[0][u] = {0}

        for step in range(k):
            current_dp = dp[step]
            next_dp = dp[step + 1]
            for u, v, w in edges:
                if u not in current_dp:
                    continue
                current_sums = current_dp[u]
                new_sums = {s + w for s in current_sums}
                if v not in next_dp:
                    next_dp[v] = set()
                next_dp[v].update(new_sums)

        mx = -1
        final_dp = dp[k]
        for node in range(n):
            if node not in final_dp:
                continue
            sums = final_dp[node]
            valid_sums = [s for s in sums if s < t]
            if valid_sums:
                current_max = max(valid_sums)
                if current_max > mx:
                    mx = current_max

        return mx
