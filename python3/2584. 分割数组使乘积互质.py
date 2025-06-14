"""
codeforces-python: 算法竞赛Python3模板库
#1: 埃氏筛
https://github.com/xile42/codeforces-python/blob/main/templates/math.py
"""
class EratosthenesSieve:

    def __init__(self, mx: int=10 ** 5 + 2, need_factors: bool=False) -> None:

        self.is_prime = [True] * mx
        self.is_prime[0] = self.is_prime[1] = False  # 忽略了越界检查

        if need_factors:
            self.factors = [[] for _ in range(mx)]  # 无重复质因数列表

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


es = EratosthenesSieve(mx=10 ** 6 + 2, need_factors=True)


class Solution:

    def findValidSplit(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return -1

        mn = defaultdict(lambda: inf)
        mx = defaultdict(lambda: -inf)
        c = Counter()

        for i, n in enumerate(nums):
            for factor in es.factors[n]:
                c[factor] += 1
                mn[factor] = min(mn[factor], i - 1)
                mx[factor] = max(mx[factor], i)

        intervals = list()
        for k in c:
            if c[k] <= 1:
                continue
            intervals.append([mn[k] + 1, mx[k] - 1])

        intervals.sort(key=lambda x: x[0])

        if not intervals or intervals[0][0] > 0:
            return 0

        merged_intervals = list()
        cur_start, cur_end = intervals[0]
        for start, end in intervals[1:]:
            if start <= cur_end + 1:
                cur_end = max(cur_end, end)
                continue
            else:
                merged_intervals.append([cur_start, cur_end])
                cur_start, cur_end = start, end
        merged_intervals.append([cur_start, cur_end])

        for start, end in merged_intervals:
            if 0 <= end + 1 < len(nums) - 1:
                return end + 1

        return -1
