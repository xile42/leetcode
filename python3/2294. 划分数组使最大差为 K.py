class Solution:

    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()
        cur = nums[0]
        ans = 1
        for v in nums[1:]:
            if v - cur > k:
                ans += 1
                cur = v

        return ans
