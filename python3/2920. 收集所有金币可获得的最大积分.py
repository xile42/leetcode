class Solution:

    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:

        g = defaultdict(list)
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        @cache
        def dfs(node, times, parent):

            cur = coins[node]
            for _ in range(times):
                cur = floor(cur / 2)

            ans1 = cur - k
            for next_node in g[node]:
                if next_node != parent:
                    ans1 += dfs(next_node, times, node)

            ans2 = floor(cur / 2)
            for next_node in g[node]:
                if next_node != parent and times <= 14:
                    ans2 += dfs(next_node, times + 1, node)

            return max(ans1, ans2)

        ans = dfs(0, 0, -1)

        return ans
