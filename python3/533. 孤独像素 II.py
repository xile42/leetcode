"""
codeforces-python: 算法竞赛Python3模板库
#2: 哈希并查集
https://github.com/xile42/codeforces-python/blob/main/templates/union_find.py
"""
class HashUnionFind:

    def __init__(self) -> None:

        self.root = dict()
        self.size = {}  # 并查集大小/秩
        self.count = 0  # 连通分量数

    # # 递归写法
    # def find(self, x: Hashable) -> Hashable:
    #
    #     if x not in self.root:
    #         self.root[x] = x
    #         self.size[x] = 1
    #         self.count += 1
    #         return x
    #
    #     if x != self.root[x]:
    #         self.root[x] = self.find(self.root[x])
    #
    #     return self.root[x]

    # 非递归写法, 效率更优
    def find(self, x: Hashable) -> Hashable:

        if x not in self.root:
            self.root[x] = x
            self.size[x] = 1
            self.count += 1
            return x

        root = x
        while self.root[root] != root:
            root = self.root[root]
        while self.root[x] != root:
            self.root[x], x = root, self.root[x]

        return root

    def merge(self, x: Hashable, y: Hashable) -> Optional[Hashable]:

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

    def is_merged(self, x: Hashable, y: Hashable) -> bool:

        return self.find(x) == self.find(y)

    def get_parts(self) -> DefaultDict[Hashable, List[Hashable]]:

        parts = defaultdict(list)
        for key in self.root:
            parts[self.find(key)].append(key)

        return parts

    def get_sizes(self) -> DefaultDict[Hashable, int]:

        sizes = defaultdict(int)
        for key in self.root:
            sizes[self.find(key)] = self.size[self.find(key)]

        return sizes


class Solution:

    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:

        uf = HashUnionFind()
        for i, row in enumerate(picture):
            key = tuple(row)
            uf.merge(i, key)

        m, n = len(picture), len(picture[0])
        row_cnt = Counter()
        col_cnt = Counter()
        col_first_black = dict()
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_cnt[i] += 1
                    col_cnt[j] += 1
                    if j not in col_first_black:
                        col_first_black[j] = i

        valid_col = set()
        sizes = uf.get_sizes()
        for j in range(n):
            if col_cnt[j] == target:
                i = col_first_black[j]
                size = sizes[uf.find(tuple(picture[i]))]
                if size - 1 == target:
                    valid_col.add(j)

        ans = 0
        for i in range(m):
            if row_cnt[i] == target:
                for j in valid_col:
                    if picture[i][j] == 'B':
                        ans += 1

        return ans
