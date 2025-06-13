class Solution:

    def minimizeMax(self, nums: List[int], p: int) -> int:

        nums.sort()

        def check(x):

            ans = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= x:
                    ans += 1
                    i += 2
                else:
                    i += 1

            return ans >= p

        l, r = 0, nums[-1] - nums[0]
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
