class Solution:

    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        g = [[] for _ in range(n)]
        in_degree = [0 for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            in_degree[v] += 1

        candidates = [i for i in range(n) if in_degree[i] == 0]
        if len(candidates) != 1:
            return -1

        vis = [False] * n
        q = deque([candidates[0]])
        while q:
            u = q.popleft()
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    q.append(v)

        return candidates[0] if all(vis) else -1
