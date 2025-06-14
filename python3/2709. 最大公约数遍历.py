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


"""
codeforces-python: 算法竞赛Python3模板库
#1: 基础埃氏筛
https://github.com/xile42/codeforces-python/blob/main/templates/math.py
"""
class EratosthenesSieve:

    def __init__(self, mx: int=10 ** 5 + 2, need_factors: bool=False) -> None:

        self.is_prime = [True] * mx
        self.is_prime[0] = self.is_prime[1] = False

        if need_factors:
            self.factors = [[] for _ in range(mx)]

        for i in range(2, mx):

            if not self.is_prime[i]:
                continue

            if need_factors:
                self.factors[i].append(i)

            for j in range((i + i) if need_factors else (i * i), mx, i):  # 仅筛质数可以从i * i开始, 求质因数只能从i + i开始; 前者更快但不影响时间复杂度
                self.is_prime[j] = False
                if need_factors:
                    self.factors[j].append(i)

    def prime_list(self) -> List[int]:

        return [i for i in range(len(self.is_prime)) if self.is_prime[i]]


es = EratosthenesSieve(need_factors=True)


class Solution:

    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        uf = HashUnionFind()
        base = 10 ** 5

        for i, n in enumerate(nums):
            if n == 1:
                return False
            if not es.factors[n]:
                uf.merge(i, base + n)
            for factor in es.factors[n]:
                uf.merge(i, base + factor)

        return uf.count == 1
