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

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        uf = UnionFind(row * col + 2)
        start = row * col
        end = start + 1
        s = set()

        for x in range(row):
            uf.merge(x * col, start)
            uf.merge(x * col + col - 1, end)

        for i, (_x, _y) in enumerate(cells):

            x, y = _x - 1, _y - 1
            for xx, yy in (x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y):
                if 0 <= xx < row and 0 <= yy < col and (xx, yy) in s:
                    uf.merge(x * col + y, xx * col + yy)

            if uf.is_merged(start, end):
                return i

            s.add((x, y))
