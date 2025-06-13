"""
codeforces-python: 算法竞赛Python3模板库
#1: 基础并查集
https://github.com/xile42/codeforces-python/blob/main/templates/union_find.py
"""
class UnionFind:

    def __init__(self, n: int) -> None:

        self.root = list(range(n))
        self.size = [1] * n  # 并查集大小/秩
        self.count = n  # 连通分量数

    # # 递归写法
    # def find(self, x):
    #
    #     if x != self.root[x]:
    #         self.root[x] = self.find(self.root[x])
    #
    #     return self.root[x]

    # 非递归写法, 效率更优
    def find(self, x: int) -> int:

        root = x
        while self.root[root] != root:
            root = self.root[root]
        while self.root[x] != root:
            self.root[x], x = root, self.root[x]

        return root

    def merge(self, x: int, y: int) -> Optional[int]:

        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return None  # 未发生合并
        # 按秩合并
        if self.size[root_x] >= self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.size[root_x] = 0
        self.count -= 1

        return root_y

    def is_merged(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)

    def get_parts(self) -> DefaultDict[int, List[int]]:

        parts = defaultdict(list)
        n = len(self.root)
        for i in range(n):
            parts[self.find(i)].append(i)

        return parts

    def get_sizes(self) -> DefaultDict[int, int]:

        sizes = defaultdict(int)
        n = len(self.root)
        for i in range(n):
            sizes[self.find(i)] = self.size[self.find(i)]

        return sizes


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        uf1 = UnionFind(n)
        uf2 = UnionFind(n)
        s1 = set()
        s2 = set()
        edges.sort(key=lambda x: x[0], reverse=True)
        ans = 0

        for t, u, v in edges:
            if t == 3 or t == 1:
                if not uf1.is_merged(u - 1, v - 1):
                    uf1.merge(u - 1, v - 1)
                else:
                    if t == 1:
                        ans += 1
                    else:
                        s1.add((u - 1, v - 1))
            if t == 3 or t == 2:
                if not uf2.is_merged(u - 1, v - 1):
                    uf2.merge(u - 1, v - 1)
                else:
                    if t == 2:
                        ans += 1
                    else:
                        s2.add((u - 1, v - 1))

        if uf1.count != 1 or uf2.count != 1:
            return -1

        return ans + len(s1 & s2)
