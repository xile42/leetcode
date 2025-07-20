max = lambda a, b: a if a > b else b
min = lambda a, b: a if a < b else b


class Solution:

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n = len(online)

        def check(x):

            degree = [0] * n
            g = [[] for _ in range(n)]

            for u, v, w in edges:
                if online[u] and online[v] and v != 0 and w >= x:
                    g[u].append((v, w))
                    degree[v] += 1

            dp = [inf] * n
            dp[0] = 0
            q = deque()

            for i in range(n):
                if degree[i] == 0:
                    q.append(i)

            while q:
                u = q.popleft()
                for v, w in g[u]:
                    dis = dp[u] + w
                    if dis < dp[v]:
                        dp[v] = dis
                    degree[v] -= 1
                    if degree[v] == 0:
                        q.append(v)

            return dp[n - 1] <= k

        left, right = 0, 10 ** 9 + 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
