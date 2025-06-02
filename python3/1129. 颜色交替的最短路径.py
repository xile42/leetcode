class Solution:

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(n)]
        for u, v in redEdges:
            g1[u].append(v)
        for u, v in blueEdges:
            g2[u].append(v)
        gs = [g1, g2]

        ans = [-1] * n
        ans[0] = 0

        vis = set()
        q = deque()
        q.append((0, 0))
        q.append((0, 1))
        vis.add((0, 0))
        vis.add((0, 1))
        dis = 1
        while q:
            next_q = deque()
            for i, flag in q:
                for j in gs[flag][i]:
                    if (j, flag) not in vis or dis < ans[j]:
                        vis.add((j, flag))
                        next_q.append((j, 1 - flag))
                        ans[j] = dis if ans[j] == -1 else min(ans[j], dis)
            q = next_q
            dis += 1

        return ans
