class Solution:

    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        root = 0
        parent = [-1] * (n + 1)
        depth = [-1] * (n + 1)
        dist = [0] * (n + 1)
        visited = [False] * (n + 1)
        q = deque([root])
        visited[root] = True
        parent[root] = root
        depth[root] = 0
        dist[root] = 0

        while q:
            u = q.popleft()
            for v, w in g[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    dist[v] = dist[u] + w
                    q.append(v)

        class LCA:

            def __init__(self, parent, depth):

                self.n = len(parent)
                self.num = (self.n).bit_length()
                self.depth = depth[:]
                self.parent = [[-1] * self.n for _ in range(self.num)]
                self.parent[0] = parent[:]

                for k in range(self.num - 1):
                    for v in range(self.n):
                        if self.parent[k][v] == -1:
                            self.parent[k + 1][v] = -1
                        else:
                            self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]

            def getLCA(self, u, v):

                if self.depth[u] > self.depth[v]:
                    u, v = v, u
                for k in range(self.num):
                    if (self.depth[v] - self.depth[u]) >> k & 1:
                        v = self.parent[k][v]
                if u == v:
                    return u
                for k in reversed(range(self.num)):
                    if self.parent[k][u] != self.parent[k][v]:
                        u = self.parent[k][u]
                        v = self.parent[k][v]

                return self.parent[0][u]

        lca = LCA(parent, depth)

        def get_dis(u, v):

            ancestor = lca.getLCA(u, v)

            return dist[u] + dist[v] - 2 * dist[ancestor]

        ans = list()
        for src1, src2, dst in queries:
            d1 = get_dis(src1, dst)
            d2 = get_dis(src2, dst)
            d3 = get_dis(src1, src2)
            total = (d1 + d2 + d3) // 2
            ans.append(total)

        return ans

        # n = len(edges) + 1
        #
        # def floyd(edges):
        #
        #     dis = [[inf] * n for _ in range(n)]
        #
        #     for i in range(n):
        #         dis[i][i] = 0
        #
        #     for u, v, w in edges:
        #         dis[u][v] = w
        #         dis[v][u] = w
        #
        #     for k in range(n):
        #         for i in range(n):
        #             for j in range(n):
        #                 if dis[i][k] + dis[k][j] < dis[i][j]:
        #                     dis[i][j] = dis[i][k] + dis[k][j]
        #
        #     return dis
        #
        # dis = floyd(edges)
        #
        # ans = list()
        # for src1, src2, dst in queries:
        #     d1 = dis[src1]
        #     d2 = dis[src2]
        #     d3 = dis[dst]
        #
        #     ans.append(min(sum(d) for d in zip(d1, d2, d3)))
        #
        # return ans

        # n = len(edges) + 1
        # g = [[] for _ in range(n)]
        # for x, y, wt in edges:
        #     g[x].append((y, wt))
        #     g[y].append((x, wt))

        # # 超时QAQ
        # @cache
        # def dijkstra(start):
        #
        #     dis = [inf] * n
        #     dis[start] = 0
        #     pq = [(0, start)]
        #     while pq:
        #         d, x = heappop(pq)
        #         if d > dis[x]:
        #             continue
        #         for y, wt in g[x]:
        #             new_d = dis[x] + wt
        #             if new_d < dis[y]:
        #                 dis[y] = new_d
        #                 heappush(pq, (new_d, y))
        #
        #     return dis
        #
        #
        # ans = list()
        # for src1, src2, dst in queries:
        #     d1 = dijkstra(src1)
        #     d2 = dijkstra(src2)
        #     d3 = dijkstra(dst)
        #
        #     ans.append(min(sum(d) for d in zip(d1, d2, d3)))
        #
        # return ans



