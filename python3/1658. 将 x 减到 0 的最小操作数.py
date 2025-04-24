class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:

        k = sum(nums) - x
        if k < 0:
            return -1
        if k == 0:
            return len(nums)

        ans = inf
        left = 0
        cur = 0
        for right, n in enumerate(nums):
            cur += n
            while cur > k:
                cur -= nums[left]
                left += 1
            if cur == k:
                ans = min(ans, len(nums) - (right - left + 1))

        return ans if ans < inf else -1
