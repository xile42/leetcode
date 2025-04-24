class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        vis = set()

        def f(i):

            nonlocal vis
            vis.add(i)

            for j in range(n):
                if isConnected[i][j] == 1 and j not in vis:
                    f(j)

        ans = 0
        for i in range(n):
            if i not in vis:
                f(i)
                ans += 1

        return ans
