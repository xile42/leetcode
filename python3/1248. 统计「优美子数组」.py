class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        def f(k):

            ans = left = 0
            cnt = 0
            for right in range(len(nums)):
                if nums[right] & 1:
                    cnt += 1
                while cnt > k:
                    if nums[left] & 1:
                        cnt -= 1
                    left += 1
                ans += right - left + 1

            return ans

        return f(k) - f(k - 1)
