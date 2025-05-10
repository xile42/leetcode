from itertools import accumulate


class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        n = len(arr)
        pre = [inf] * (n + 1)
        left = 0
        ans = inf
        acc = list(accumulate(arr))
        for right in range(n):
            while acc[right] - (0 if left == 0 else acc[left - 1]) > target:
                left += 1
            if acc[right] - (0 if left == 0 else acc[left - 1]) == target:
                ans = min(ans, pre[left] + right - left + 1)
                pre[right + 1] = min(pre[right], right - left + 1)
            else:
                pre[right + 1] = pre[right]

        return ans if ans < inf else -1
