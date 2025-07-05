"""
codeforces-python: 算法竞赛Python3模板库
#1: 一维差分(哈希表实现)
https://github.com/xile42/codeforces-python/blob/main/templates/diff.py
"""
class DiffArray:

    @staticmethod
    def valid_points_count(lrws: List[Tuple[int, int, int]], check: Callable[[int], bool]=lambda x: x > 0) -> int:
        """计算区间[l, r], 全部更新后, 值满足check的整点数"""
        diff = defaultdict(int)
        for l, r, w in lrws:
            diff[l] += w
            diff[r + 1] -= w

        xs = sorted(diff.keys())
        ans = cur = 0
        for i in range(len(xs)):
            if i > 0 and check(cur):
                ans += xs[i] - xs[i - 1]
            cur += diff[xs[i]]

        return ans

    @staticmethod
    def covered_points_count(lrs: List[Tuple[int, int]]) -> int:
        """计算区间[l, r], 全部更新后, 至少被一个区间覆盖的整点数"""
        diff = defaultdict(int)
        for l, r in lrs:
            diff[l] += 1
            diff[r + 1] -= 1

        xs = sorted(diff.keys())
        ans = cur = 0
        for i in range(1, len(xs)):
            if cur > 0:
                ans += xs[i] - xs[i - 1]
            cur += diff[xs[i]]

        return ans

    @staticmethod
    def max_covered_times(lrs: List[Tuple[int, int]]) -> int:
        """计算区间[l, r], 全部更新后, 整点最大重叠层数"""
        diff = defaultdict(int)
        for l, r in lrs:
            diff[l] += 1
            diff[r + 1] -= 1

        xs = sorted(diff.keys())
        ans = cur = 0
        for i in range(1, len(xs)):
            cur += diff[xs[i - 1]]
            if cur > ans:
                ans = cur

        return ans

    @staticmethod
    def merge_intervals(lrs: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        """合并区间"""
        diff = defaultdict(int)
        for l, r in lrs:
            diff[l] += 1
            diff[r + 1] -= 1

        xs = sorted(diff.keys())
        ans = list()
        cur = start = 0
        for i in range(len(xs)):
            if cur > 0 and start == 0:  # 进入覆盖区
                start = xs[i]
            elif cur == 0 and start > 0:  # 离开覆盖区
                ans.append((start, xs[i] - 1))
                start = 0
            cur += diff[xs[i]]

        return ans

    @staticmethod
    def batch_query(lrws: List[Tuple[int, int, int]], queries: List[int]) -> List[int]:
        """更新所有操作后, 批量查询对应点的值"""
        diff = defaultdict(int)
        for l, r, w in lrws:
            diff[l] += w
            diff[r + 1] -= w

        xs = sorted(diff.keys())
        prefix = list()
        cur = 0
        for x in xs:
            cur += diff[x]
            prefix.append((x, cur))

        ans = list()
        for q in queries:
            idx = bisect.bisect_right(xs, q) - 1
            ans.append(prefix[idx][1] if idx >= 0 else 0)

        return ans

    @staticmethod
    def diff_accumulate(lrws: List[Tuple[int, int, int]]) -> List[int]:
        """更新所有操作后, 返回所有点的值"""
        diff = defaultdict(int)
        for l, r, w in lrws:
            diff[l] += w
            diff[r + 1] -= w  # 对于两个区间重合端点, 如(l, x)和(x, r), 若二者同时生效, 这里为r + 1, 否则(如人立刻下车)为r

        xs = sorted(diff.keys())
        prefix = list()
        cur = 0
        for x in xs:
            cur += diff[x]
            prefix.append(cur)

        return prefix[:-1]


class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        base = 10 ** 9 + 7
        lrws = [[i, i, 0] for i in range(len(nums))] + [[s, e, 1] for s, e in requests]
        factors = DiffArray.diff_accumulate(lrws)

        ans = 0
        factors.sort()
        nums.sort()
        for f, n in zip(factors, nums):
            ans += (f * n) % base
            ans %= base

        return ans
