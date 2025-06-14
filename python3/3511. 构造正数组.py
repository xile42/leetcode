class Solution:

    def makeArrayPositive(self, nums: List[int]) -> int:

        ans = 0
        n = len(nums)
        presum = [nums[0]]
        premax = [0, max(nums[0], 0)]
        for i in range(1, n):
            cur = presum[-1] + nums[i]
            if i - 2 >= 0 and cur <= premax[i - 2]:
                ans += 1
                cur = cur - nums[i] + 10 ** 18
            presum.append(cur)
            premax.append(max(premax[-1], cur))

        return ans
