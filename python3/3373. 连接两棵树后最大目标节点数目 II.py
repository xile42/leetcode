nodes = defaultdict(set)


class Solution:

    def build_tree(self, edges: List[List[int]]):

        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int, d: int, fetch=False):

            global nodes
            if fetch:
                nodes[d & 1].add(x)
            even, odd = 1, 0
            for y in g[x]:
                if y != fa:
                    _even, _odd = dfs(y, x, d + 1, fetch)
                    even += _odd
                    odd += _even

            return even, odd

        return dfs

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        global nodes
        nodes = defaultdict(set)
        dfs = self.build_tree(edges2)
        max2 = max(dfs(0, -1, 0))

        dfs = self.build_tree(edges1)
        dfs(0, -1, 0, True)
        pos = 0 if 0 in nodes[0] else 1

        ans = list()
        for i in range(len(edges1) + 1):
            if i in nodes[pos]:
                ans.append(len(nodes[pos]) + max2)
            else:
                ans.append(len(nodes[1 - pos]) + max2)

        return ans
