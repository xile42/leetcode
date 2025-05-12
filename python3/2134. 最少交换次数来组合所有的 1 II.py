class Solution:

    def minSwaps(self, nums: List[int]) -> int:

        ns = nums + nums
        k = sum(nums)
        ans = inf
        s = 0
        for i, n in enumerate(ns):
            if i >= len(nums) + k:
                break
            s += n
            if i >= k:
                s -= ns[i - k]
            if i >= k - 1:
                ans = min(ans, k - s)

        return ans
