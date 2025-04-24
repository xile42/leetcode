class Solution:

    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        diff = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            diff.append(nums[i] - nums[i - 1])

        # print("init", diff)

        def update(l, r):

            nonlocal diff
            diff[l] -= 1
            if r != n - 1:
                diff[r + 1] += 1

            # print("update", diff, l, r)

        for l, r in queries:
            update(l, r)

        # print("diff", diff)

        result = [diff[0]]
        for i in range(1, n):
            result.append(result[-1] + diff[i])

        # print("result", result)

        return all(i <= 0 for i in result)
