"""
codeforces-python: 算法竞赛Python3模板库
#1: 基础并查集
https://github.com/xile42/codeforces-python/blob/main/templates/union_find.py
"""
from collections import defaultdict


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

    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        uf = UnionFind(c + 1)
        for u, v in connections:
            uf.merge(u, v)

        parts = uf.get_parts()
        cur_idx = dict()
        for k in parts:
            parts[k].sort()
            cur_idx[k] = 0
        invalid = set()

        ans = list()
        for op, x in queries:
            if op == 1:
                if x not in invalid:
                    ans.append(x)
                else:
                    k = uf.find(x)
                    while cur_idx[k] < len(parts[k]) and parts[k][cur_idx[k]] in invalid:
                        cur_idx[k] += 1
                    if cur_idx[k] < len(parts[k]):
                        ans.append(parts[k][cur_idx[k]])
                    else:
                        ans.append(-1)
            if op == 2:
                invalid.add(x)

        return ans
