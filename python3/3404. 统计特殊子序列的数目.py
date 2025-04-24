class Solution:

    def numberOfSubsequences(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0
        cnt = Counter()
        for i in range(4, n - 2):
            q = nums[i - 2]
            r = nums[i]
            for _, p in enumerate(nums[:i - 3]):
                cnt[p / q] += 1
            for _, s in enumerate(nums[i + 2:]):
                ans += cnt[s / r]

        return ans
