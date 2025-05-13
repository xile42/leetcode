class Solution:

    def minimizeArrayValue(self, nums: List[int]) -> int:

        def check(x):

            cur = 0
            for i in range(len(nums) - 1, 0, -1):
                cur = max(nums[i] + cur - x, 0)

            return cur + nums[0] <= x

        left = 0
        right = max(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
