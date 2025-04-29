class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph)
        ans = list()
        vis = [False] * n
        vis[0] = True

        def f(i, path):

            if i == n - 1:
                ans.append(path + [i])
                return

            for j in graph[i]:
                vis[j] = True
                f(j, path + [i])
                vis[j] = False

        f(0, list())

        return ans
