### 题目不一定入库，这里备份

# 2025 年浦东新区人工智能创新应用竞赛 Q4 棋盘整理
# 链接：https://leetcode.cn/contest/2025_pudong_ai/problems/1Hxnb6/


# 现在有一盘已经结束的围棋，棋盘可以视为无限大，棋子的坐标由二维数组pieces表示，其每个元素为[x, y]。
# 为了快速的整理好棋子，现在希望能将所有棋子整理成 连续的一排，必须与x轴平行 或y轴平行。
# 求所有棋子需要移动的曼哈顿距离之和的最小值。由于答案可能很大，请你返回答案对10^9 + 7取余的结果


# 2 <= pieces.length <= 10^5
# pieces[i].length = 2
# -10^9 <= pieces[i][0], pieces[i][1] <= 10^9


"""
codeforces-python: 算法竞赛Python3模板库
#2: 一维距离和
https://github.com/xile42/codeforces-python/blob/main/templates/prefix_sum.py
"""
class DistancePrefixSum:

    def __init__(self, arr: List[int], is_sorted: bool = False):

        self.n = len(arr)
        self.arr = sorted(arr) if not is_sorted else arr
        self.prefix = [0] * (self.n + 1)

        for i in range(self.n):
            self.prefix[i + 1] = self.prefix[i] + self.arr[i]

    def query(self, target: Optional[int]=None, l: int=0, r: Optional[int]=None) -> int:
        """ sum(abs(a[i] - target)) for i in [l, r] """

        target = self.arr[self.n // 2] if target is None else target
        r = self.n - 1 if r is None else r
        i = bisect.bisect_left(self.arr, target, l, r + 1)
        left = target * (i - l) - (self.prefix[i] - self.prefix[l])
        right = (self.prefix[r + 1] - self.prefix[i]) - target * (r + 1 - i)

        return left + right


class Solution:

    def organizeChessboard(self, pieces: List[List[int]]) -> int:

        xs = [p[0] for p in pieces]
        ys = [p[1] for p in pieces]
        n = len(pieces)
        base = 10 ** 9 + 7

        y_sum = DistancePrefixSum(ys).query()
        xs_sorted = sorted(xs)
        b = [xs_sorted[i] - i for i in range(n)]
        x_sum_hor = DistancePrefixSum(b).query()
        total_hor = x_sum_hor + y_sum

        x_sum = DistancePrefixSum(xs).query()
        ys_sorted = sorted(ys)
        c = [ys_sorted[i] - i for i in range(n)]
        y_sum_ver = DistancePrefixSum(c).query()
        total_ver = x_sum + y_sum_ver

        ans = min(total_hor, total_ver) % base

        return ans
