import typing


class SegTree:

    def __init__(
            self,
            op: typing.Callable[[typing.Any, typing.Any], typing.Any],  # 二元操作函数，用于合并两节点值
            e: typing.Any,  # 单位元(identity element)，对任意x，op(x, e) = ope(e, x) = x
            v: typing.Union[int, typing.List[typing.Any]]  # 初始数据，列表长度或列表
        ) -> None:

        self._op = op
        self._e = e

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = (self._n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)

        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:  # 单点更新，递归向上

        assert 0 <= p < self._n

        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:

        assert 0 <= p < self._n

        return self._d[p + self._size]

    def prod(self, left: int, right: typing.Optional[int] = None) -> typing.Any:  # 区间查询 [left, right) 合并结果

        if right is None:
            right = self._n

        assert 0 <= left <= right <= self._n

        sml = self._e
        smr = self._e
        left += self._size
        right += self._size

        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:  # 全局查询 整个数组合并结果

        return self._d[1]

    def max_right(self, left: int, f: typing.Callable[[typing.Any], bool]) -> int:  # 最大右边界right 使得 [left, right) 满足f

        assert 0 <= left <= self._n
        assert f(self._e)

        if left == self._n:
            return self._n

        left += self._size
        sm = self._e

        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not f(self._op(sm, self._d[left])):
                while left < self._size:
                    left *= 2
                    if f(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, f: typing.Callable[[typing.Any], bool]) -> int:  # 最小左边界left 使得 [left, right) 满足f

        assert 0 <= right <= self._n
        assert f(self._e)

        if right == 0:
            return 0

        right += self._size
        sm = self._e

        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not f(self._op(self._d[right], sm)):
                while right < self._size:
                    right = 2 * right + 1
                    if f(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:  # 更新节点k为子节点合并值

        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


class Solution:

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:

        n = len(s)
        ns = [[c, 1, 1, 1, 1, c] for c in s]

        def merge(a, b):

            first_a, pre_a, mx_a, suf_a, len_a, last_a = a
            first_b, pre_b, mx_b, suf_b, len_b, last_b = b

            if first_a == -1:
                return b
            elif first_b == -1:
                return a

            if last_a == first_b:
                mx_c = max(suf_a + pre_b, mx_a, mx_b)
                if pre_a == len_a:
                    pre_c = pre_a + pre_b
                else:
                    pre_c = pre_a
                if suf_b == len_b:
                    suf_c = suf_b + suf_a
                else:
                    suf_c = suf_b
                first_c = first_a
                last_c = last_b
            else:
                mx_c = max(mx_a, mx_b)
                pre_c = pre_a
                suf_c = suf_b
                first_c = first_a
                last_c = last_b

            return [first_c, pre_c, mx_c, suf_c, len_a + len_b, last_c]

        seg = SegTree(merge, [-1, 0, 0, 0, 0, -1], ns)

        # print(seg._d)

        ans = list()
        for i, c in zip(queryIndices, queryCharacters):
            seg.set(i, [c, 1, 1, 1, 1, c])
            # print(seg._d)
            root = seg.all_prod()
            ans.append(root[2])

        return ans