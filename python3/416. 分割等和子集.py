class Solution:

    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)
        if s & 1:
            return False

        t = s // 2
        success = False

        @cache
        def f(t, i):

            nonlocal success
            if t < 0 or success or len(nums[i:]) == 0:
                return

            if t == 0:
                success = True
                return

            if t >= nums[i]:
                f(t - nums[i], i + 1)
            f(t, i + 1)

        f(t, 0)

        return success
