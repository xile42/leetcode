class Solution:

    def dfs(self, cur):

        self.vis[cur] = True

        result = list()
        for i in self.g[cur]:
            if not self.vis[i]:
                result.append(self.dfs(i))
        if len(set(result)) <= 1:
            self.ans += 1

        return 1 if len(result) == 0 else sum(result) + 1

    def countGoodNodes(self, edges: List[List[int]]) -> int:

        self.ans = 0
        self.g = defaultdict(list)
        for i, j in edges:
            self.g[i].append(j)
            self.g[j].append(i)
        self.vis = [False for _ in range(len(edges) + 1)]

        self.dfs(0)

        return self.ans
