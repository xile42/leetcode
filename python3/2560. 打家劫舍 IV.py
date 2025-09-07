class Solution:

    def minCapability(self, nums: List[int], k: int) -> int:

        def check(x):

            ans = 0
            i = 0
            while i < len(nums):
                n = nums[i]
                if n <= x:
                    ans += 1
                    if ans >= k:
                        return True
                    i += 2
                else:
                    i += 1

            return False

        left = min(nums)
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
