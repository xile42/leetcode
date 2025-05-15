base = 10 ** 9 + 7


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


class Solution:

    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        vis = [False] * (n + 1)

        root = 1
        parent = [-1] * (n + 1)
        depth = [-1] * (n + 1)
        q = deque([root])
        vis[root] = True
        parent[root] = root
        depth[root] = 0

        while q:
            u = q.popleft()
            for v in g[u]:
                if not vis[v]:
                    vis[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)

        lca = LCA(parent, depth)

        def get_dis(u, v):

            ancestor = lca.getLCA(u, v)

            return depth[u] + depth[v] - 2 * depth[ancestor]

        ans = list()
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            n = get_dis(u, v)
            ans.append(pow(2, n - 1) % base)

        return ans
