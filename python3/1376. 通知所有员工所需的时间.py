class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        g = defaultdict(list)
        for i, j in enumerate(manager):
            if j != -1:
                g[j].append(i)

        def f(i):

            ans = 0
            for j in g[i]:
                ans = max(ans, f(j))

            return ans + informTime[i]

        return f(headID)
