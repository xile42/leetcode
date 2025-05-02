class Solution:

    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        ans = inf

        for length in range(l, r + 1):

            cur = sum(nums[:length])
            if cur > 0:
                ans = min(ans, cur)

            left = 0
            for right in range(length, len(nums)):
                cur += nums[right]
                cur -= nums[left]
                left += 1
                if cur > 0:
                    ans = min(ans, cur)

        return -1 if ans == inf else ans
