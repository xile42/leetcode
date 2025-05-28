from itertools import accumulate


class Solution:

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        if all(i <= 0 for i in nums):
            return 0

        def check(x):

            diff = [nums[0]]
            n = len(nums)
            for i in range(1, n):
                diff.append(nums[i] - nums[i - 1])

            def update(l, r, v):

                nonlocal diff
                diff[l] -= v
                if r != n - 1:
                    diff[r + 1] += v

            for i in range(x):
                l, r, v = queries[i]
                update(l, r, v)

            if all(i <= 0 for i in accumulate(diff)):
                return True

            return False

        left = 1
        right = len(queries)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return -1 if left == len(queries) + 1 else left
