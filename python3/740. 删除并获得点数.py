class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:

        counter = Counter(nums)
        v = dict()
        for key, value in counter.items():
            v[key] = key * value
        nums = sorted(counter.keys())
        dp = [0] * (len(nums) + 1)
        dp[1] = v[nums[0]]
##        print(nums)
        for i in range(2, len(nums) + 1):
##            print(dp)
            left_value = dp[i-1] if nums[i-2] != nums[i-1] - 1 else dp[i-2]
            dp[i] = max(left_value + v[nums[i-1]], dp[i-1])
##            print(dp, left_value)

        return dp[len(nums)]
