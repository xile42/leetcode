class Solution:

    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:

        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        def check(mxw):

            visit = set()

            def dfs(cur):

                for next_node, w in g[cur]:
                    if next_node in visit or w > mxw:
                        continue
                    visit.add(next_node)
                    dfs(next_node)

            cnt = 0
            for i in range(n):
                if i in visit:
                    continue
                dfs(i)
                cnt += 1

            return cnt <= k

        if not edges:
            return 0

        left = 0
        right = max(w for _, _, w in edges)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
