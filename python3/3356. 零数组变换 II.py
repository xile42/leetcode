from itertools import accumulate


class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        if all(i <= 0 for i in nums):
            return 0

        diff = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            diff.append(nums[i] - nums[i - 1])

        def update(l, r, v):

            nonlocal diff
            diff[l] -= v
            if r != n - 1:
                diff[r + 1] += v

            # print("update", diff, l, r)

        def f(k):

            d = diff.copy()

        for k, (l, r, v) in enumerate(queries):
            update(l, r, v)
            if all(i <= 0 for i in accumulate(diff)):
                return k + 1

        return -1
