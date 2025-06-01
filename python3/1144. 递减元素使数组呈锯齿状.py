class Solution:

    def movesToMakeZigzag(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        ans1 = 0
        n = len(nums)
        for i in range(0, n, 2):
            left = inf if i == 0 else nums[i - 1]
            right = inf if i == n - 1 else nums[i + 1]
            ans1 += max(nums[i] - min(left, right) + 1, 0)

        ans2 = 0
        n = len(nums)
        for i in range(1, n, 2):
            left = inf if i == 0 else nums[i - 1]
            right = inf if i == n - 1 else nums[i + 1]
            ans2 += max(nums[i] - min(left, right) + 1, 0)

        return min(ans1, ans2)
