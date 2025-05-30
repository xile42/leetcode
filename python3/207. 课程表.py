class Solution:

    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:

        g = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for u, v in prerequisites:
            g[v].append(u)
            indegree[u] += 1

        q = deque()
        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)

        cnt = 0
        while q:
            i = q.popleft()
            cnt += 1
            for j in g[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

        return cnt == n
