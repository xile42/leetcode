"""
codeforces-python: 算法竞赛Python3模板库
#2: 一维距离和
https://github.com/xile42/codeforces-python/blob/main/templates/prefix_sum.py
"""
class DistancePrefixSum:

    def __init__(self, arr: List[int]):

        self.n = len(arr)
        self.arr = sorted(arr)
        self.prefix = [0] * (self.n + 1)

        for i in range(self.n):
            self.prefix[i + 1] = self.prefix[i] + self.arr[i]

    def query(self, target: int, l: int=0, r: Optional[int]=None) -> int:
        """ sum(abs(a[i] - target)) for i in [l, r] """

        r = self.n - 1 if r is None else r
        i = bisect.bisect_left(self.arr, target, l, r + 1)
        left = target * (i - l) - (self.prefix[i] - self.prefix[l])
        right = (self.prefix[r + 1] - self.prefix[i]) - target * (r + 1 - i)

        return left + right


class Solution:

    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:

        prefix = DistancePrefixSum(nums)

        return [prefix.query(target) for target in queries]
