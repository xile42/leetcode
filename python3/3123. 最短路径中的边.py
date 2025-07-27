"""
codeforces-python: 算法竞赛Python3模板库
#2: Dijkstra
https://github.com/xile42/codeforces-python/blob/main/templates/graph.py
"""
class Dijkstra:

    def __init__(self, n: int, edges: List[List[int]], start: int, directed: bool = False, need_path: bool = False) -> None:

        self.n = n
        self.g = [[] for _ in range(n)]
        for u, v, w in edges:
            self.g[u].append((v, w))
            if not directed:
                self.g[v].append((u, w))

        self.start = start
        self.directed = directed
        self.need_path = need_path
        self.dis = [inf] * self.n
        self.pre = [-1] * self.n if need_path else None
        self._run()

    def _run(self) -> None:
        """ 执行Dijkstra算法计算最短路径 """

        self.dis[self.start] = 0
        heap = [(0, self.start)]

        while heap:
            dis_x, x = heappop(heap)
            if dis_x > self.dis[x]:
                continue
            for y, w in self.g[x]:
                new_dis_y = dis_x + w
                if new_dis_y < self.dis[y]:
                    self.dis[y] = new_dis_y
                    heappush(heap, (new_dis_y, y))
                    if self.need_path:
                        self.pre[y] = x

    def get_dis(self) -> List[float]:
        """ 获取起点到所有节点的最短距离列表 """

        return self.dis

    def get_dis_to_tar(self, target: int) -> float:
        """ 获取起点到目标节点的最短距离 """

        return self.dis[target]

    def get_path(self, target: int) -> Optional[List[int]]:
        """ 获取起点到目标节点的最短路径 """

        if not self.need_path:
            raise ValueError("Path recording was not enabled. Set need_path=True in constructor.")

        if self.dis[target] == inf:
            return None

        path = list()
        while target != -1:
            path.append(target)
            target = self.pre[target]
        path.reverse()

        return path

    def get_reachable_nodes(self) -> List[int]:
        """ 获取所有可达节点的列表 """

        return [i for i, d in enumerate(self.dis) if d != inf]

    def get_unreachable_nodes(self) -> List[int]:
        """ 获取所有不可达节点的列表 """

        return [i for i, d in enumerate(self.dis) if d == inf]

    def is_reachable(self, target: int) -> bool:
        """ 判断目标节点是否可达 """

        return self.dis[target] != inf


class Solution:

    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:

        dij1 = Dijkstra(n, edges, 0)
        dis1 = dij1.get_dis()
        dij2 = Dijkstra(n, edges, n - 1)
        dis2 = dij2.get_dis()

        total = dis1[n - 1]
        m = len(edges)
        if total == inf:
            return [False] * m

        ans = [False] * m
        for i, (u, v, w) in enumerate(edges):
            if dis1[u] + w + dis2[v] == total or dis1[v] + w + dis2[u] == total:
                ans[i] = True

        return ans
