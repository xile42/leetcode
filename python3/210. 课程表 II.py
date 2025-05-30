class Solution:

    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:

        g = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for u, v in prerequisites:
            g[v].append(u)
            indegree[u] += 1

        q = deque()
        for i, v in enumerate(indegree):
            if v == 0:
                q.append(i)

        ans = list()
        while q:
            i = q.popleft()
            ans.append(i)
            for j in g[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

        return list() if len(ans) != n else ans
