"""
codeforces-python: 算法竞赛Python3模板库
#1: 基础并查集
https://github.com/xile42/codeforces-python/blob/main/templates/union_find.py
"""
class UnionFind:

    def __init__(self, n: int) -> None:

        self.root = list(range(n))
        self.size = [1] * n  # 并查集大小/秩
        self.part = n  # 连通分量数

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
        self.part -= 1

        return root_y

    def is_merged(self, x: int, y: int) -> bool:

        return self.find(x) == self.find(y)

    def get_parts(self):

        parts = defaultdict(list)
        n = len(self.root)
        for i in range(n):
            parts[self.find(i)].append(i)

        return parts

    def get_sizes(self):

        sizes = defaultdict(int)
        n = len(self.root)
        for i in range(n):
            sizes[self.find(i)] = self.size[self.find(i)]

        return sizes


class Solution:

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        uf = UnionFind(n)

        for i in range(1, n):
            if abs(nums[i] - nums[i - 1]) <= maxDiff:
                uf.merge(i, i - 1)

        ans = [uf.is_merged(x, y) for x, y in queries]

        return ans
