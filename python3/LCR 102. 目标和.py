class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(lambda: defaultdict(int))
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1
        for i, n in enumerate(nums):
            if i == 0:
                continue
            for k, v in dp[i - 1].items():
                dp[i][n + k] += v
                dp[i][-n + k] += v

        return dp[len(nums) - 1][target]
