class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans = list()
        for i, n in enumerate(nums):
            sub = nums[max(0, i - n):i + 1]
            v = 0 if len(sub) == 0 else sum(sub)
            ans.append(v)

        return sum(ans)
