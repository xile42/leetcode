"""
codeforces-python: 算法竞赛Python3模板库
#1: 稀疏表(基类)
https://github.com/xile42/codeforces-python/blob/main/templates/sparse_table.py
"""
class SparseTable:

    def __init__(self, arr: List[Union[int, Tuple[int, int]]]) -> None:

        n = len(arr)
        size = n.bit_length()
        self.st = [[0] * size for _ in range(n)]

        for i in range(n):
            self.st[i][0] = arr[i]

        for j in range(1, size):
            for i in range(n - (1 << j) + 1):
                self.st[i][j] = self.op(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])

    def query(self, l: int, r: int) -> int:
        """ [l, r] """

        k = (r - l + 1).bit_length() - 1
        return self.op(self.st[l][k], self.st[r + 1 - (1 << k)][k])

    def op(self, a: int, b: int) -> int:
        """ 支持的算子包括: min, max, gcd, &, |, product, lca """

        raise NotImplementedError


"""
codeforces-python: 算法竞赛Python3模板库
#2: 稀疏表-MIN运算
https://github.com/xile42/codeforces-python/blob/main/templates/sparse_table.py
"""
class MinSparseTable(SparseTable):

    def op(self, a: int, b: int) -> int:

        return a if a < b else b  # 手写min以提高效率


"""
codeforces-python: 算法竞赛Python3模板库
#3: 稀疏表-MAX运算
https://github.com/xile42/codeforces-python/blob/main/templates/sparse_table.py
"""
class MaxSparseTable(SparseTable):

    def op(self, a: int, b: int) -> int:

        return a if a > b else b  # 手写max以提高效率


class Solution:

    def maxTotalValue(self, nums: List[int], k: int) -> int:

        n = len(nums)

        st_min = MinSparseTable(nums)
        st_max = MaxSparseTable(nums)

        vis = set()
        heap = list()
        start_value = st_max.query(0, n - 1) - st_min.query(0, n - 1)
        heappush(heap, (-start_value, 0, n - 1))
        vis.add((0, n - 1))

        ans = 0
        for _ in range(k):

            neg_val, l, r = heappop(heap)
            val = -neg_val
            ans += val

            if l + 1 <= r:
                new_l = l + 1
                if (new_l, r) not in vis:
                    vis.add((new_l, r))
                    v_new = st_max.query(new_l, r) - st_min.query(new_l, r)
                    heappush(heap, (-v_new, new_l, r))

            if r - 1 >= l:
                new_r = r - 1
                if (l, new_r) not in vis:
                    vis.add((l, new_r))
                    v_new = st_max.query(l, new_r) - st_min.query(l, new_r)
                    heappush(heap, (-v_new, l, new_r))

        return ans
