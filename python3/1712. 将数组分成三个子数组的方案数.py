class Solution:

    def waysToSplit(self, nums: List[int]) -> int:

        acc = [0] + list(accumulate(nums))
        total = acc[-1]
        n = len(nums)
        ans = 0
        base = 10 ** 9 + 7

        for i in range(n - 2):
            left = acc[i + 1]
            if left * 2 > total - left:
                break
            tar_min = left
            tar_max = (total - left) / 2
            mid_min_idx = max(i + 1, bisect_left(acc, left + tar_min) - 1)
            mid_max_idx = min(n - 1, bisect_right(acc, left + tar_max) - 1)
            ans += max(mid_max_idx - mid_min_idx, 0) % base
            ans %= base

        return ans
