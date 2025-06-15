"""
codeforces-python: 算法竞赛Python3模板库
#1: 最近公共祖先(LCA)
https://github.com/xile42/codeforces-python/blob/main/templates/tree.py
"""
class LCABinaryLifting:

    def __init__(self, edges: List[List[int]]) -> None:

        """
        注意:
            1. edges: 默认顺序为 [u, v, (w)]
            2. edges: 默认节点编号为 0 ~ n - 1
            3. 根节点: 默认为 0
        """

        n = len(edges) + 1
        self.m = n.bit_length()  # 最大跳跃步数的二进制位数

        g = [[] for _ in range(n)]
        for edge in edges:
            x, y, w = edge if len(edge) == 3 else (x, y, 1)
            g[x].append([y, w])
            g[y].append([x, w])

        self.depth = [0] * n  # 每个节点的深度
        self.dist = [0] * n  # 每个节点到根节点的带权距离
        self.parent = [[-1] * self.m for _ in range(n)]  # 倍增祖先数组, parent[x][k]表示节点x的2^k个祖先, 超出root则为-1

        def dfs(x: int, fa: int) -> None:

            self.parent[x][0] = fa
            for y, w in g[x]:
                if y != fa:
                    self.depth[y] = self.depth[x] + 1
                    self.dist[y] = self.dist[x] + w
                    dfs(y, x)

        dfs(0, -1)  # 假设根节点是0

        for i in range(self.m - 1):
            for x in range(n):
                if (p := self.parent[x][i]) != -1:
                    self.parent[x][i + 1] = self.parent[p][i]

    def kth_ancestor(self, node: int, k: int) -> int:

        for i in range(k.bit_length()):
            if k >> i & 1:
                node = self.parent[node][i]
                if node == -1:
                    break

        return node  # -1 if not exists

    def lca(self, x: int, y: int) -> int:

        if self.depth[x] > self.depth[y]:
            x, y = y, x

        y = self.kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x

        for i in range(self.m - 1, -1, -1):
            px, py = self.parent[x][i], self.parent[y][i]
            if px != py:
                x, y = px, py

        return self.parent[x][0]

    def get_dis(self, x: int, y: int) -> int:

        return self.dist[x] + self.dist[y] - 2 * self.dist[self.lca(x, y)]

    def up_dis(self, x: int, d: int) -> int:  # 上跳至多距离d

        dx = self.dist[x]
        for i in range(self.m - 1, -1, -1):
            p = self.parent[x][i]
            if p != -1 and dx - self.dist[p] <= d:
                x = p

        return x


class Solution:

    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:

        lca = LCABinaryLifting(edges)

        ans = list()
        for u, v in queries:
            lca_node = lca.lca(u, v)
            d1 = lca.dist[u] - lca.dist[lca_node]
            d2 = lca.dist[v] - lca.dist[lca_node]
            half = ceil((d1 + d2) / 2)
            if d1 == d2:
                ans.append(lca_node)
            elif d1 > d2:
                node = lca.up_dis(u, half - 1)
                ans.append(lca.parent[node][0])
            else:
                node = lca.up_dis(v, d1 + d2 - half)
                ans.append(node)

        return ans
