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


max = lambda x, y: x if x > y else y
min = lambda x, y: x if x < y else y


class Solution:

    def minTime(self, s: str, order: List[int], k: int) -> int:

        n = len(s)
        total = n * (n + 1) // 2
        uf = UnionFind(n)
        left = list(range(n))
        right = list(range(n))

        active = [False] * n
        cur = 0

        if total < k:
            return -1

        for t in range(n - 1, -1, -1):

            i = order[t]
            active[i] = True
            cur += 1

            for j in (i + 1, i - 1):

                if j < 0 or j >= n or not active[j]:
                    continue

                root_i = uf.find(i)
                root_j = uf.find(j)

                len_i = right[root_i] - left[root_i] + 1
                len_j = right[root_j] - left[root_j] + 1
                val_i = len_i * (len_i + 1) // 2
                val_j = len_j * (len_j + 1) // 2

                new_root = uf.merge(i, j)

                new_left = min(left[root_i], left[root_j])
                new_right = max(right[root_i], right[root_j])
                left[new_root] = new_left
                right[new_root] = new_right

                len_new = new_right - new_left + 1
                val_new = len_new * (len_new + 1) // 2
                increase = val_new - (val_i + val_j)
                cur += increase

            cur_valid = total - cur
            if cur_valid < k:
                return t
