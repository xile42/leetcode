# 灵神模板
# https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/
class SegmentTree:

    def __init__(self, n: int, init_val=0):
        if isinstance(init_val, int):
            init_val = [init_val] * n
        self._n = n
        self._tree = [0] * (2 << (n - 1).bit_length())
        self._build(init_val, 1, 0, n - 1)

    def _merge_val(self, a: int, b: int) -> int:
        return a + b

    def _maintain(self, node: int) -> None:
        self._tree[node] = self._merge_val(self._tree[node * 2], self._tree[node * 2 + 1])

    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        if l == r:
            self._tree[node] = a[l]
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)
        self._build(a, node * 2 + 1, m + 1, r)
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self._tree[node] = val
            return
        m = (l + r) // 2
        if i <= m:
            self._update(node * 2, l, m, i, val)
        else:
            self._update(node * 2 + 1, m + 1, r, i, val)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self._tree[node]
        m = (l + r) // 2
        if qr <= m:
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)

    def get(self, i: int) -> int:
        return self._query(1, 0, self._n - 1, i, i)


class Solution:

    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        @cache
        def f(x):

            if x == 1:
                return 0

            return f(bin(x).count('1')) + 1

        n = len(nums)
        depth = [0] * n
        for i in range(n):
            depth[i] = f(nums[i])

        trees = list()
        for k_val in range(5):
            init_ns = [1 if depth[i] == k_val else 0 for i in range(n)]
            trees.append(SegmentTree(n, init_ns))

        ans = list()
        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                if k >= 5:
                    ans.append(0)
                else:
                    ans.append(trees[k].query(l, r))
            else:
                _, idx, val = q
                old_depth = depth[idx]
                new_depth = f(val)
                depth[idx] = new_depth
                trees[old_depth].update(idx, 0)
                trees[new_depth].update(idx, 1)

        return ans
