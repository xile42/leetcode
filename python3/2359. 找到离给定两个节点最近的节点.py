from copy import deepcopy


class Solution:

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        n = len(edges)
        g = [[] for _ in range(n)]
        for u, v in enumerate(edges):
            if v != -1:
                g[u].append(v)

        vis = [False for _ in range(n)]
        dis = dict()

        def dfs(i, d):

            vis[i] = True
            dis[i] = d
            for j in g[i]:
                if not vis[j]:
                    dfs(j, d + 1)

        dfs(node1, 0)
        dis1 = deepcopy(dis)
        vis = [False for _ in range(n)]
        dis = dict()
        dfs(node2, 0)
        dis2 = deepcopy(dis)

        nodes = dis1.keys() & dis2.keys()
        if not nodes:
            return -1

        ns = [[max(dis1[k], dis2[k]), k] for k in nodes]
        ns.sort()

        return ns[0][1]
