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

    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        d = defaultdict(list)

        def f(node, depth):

            if node is None:
                return

            d[depth].append(node.val)
            f(node.left, depth + 1)
            f(node.right, depth + 1)

        f(root, 0)

        ans = 0
        for vs in d.values():
            svs = sorted(vs)
            uf = HashUnionFind()
            for i, j in zip(vs, svs):
                uf.merge(i, j)
            ans += len(vs) - uf.count

        return ans
