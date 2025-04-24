class Solution:

    def missingInteger(self, nums: List[int]) -> int:

        diffs = [True if i == 0 or nums[i] == nums[i - 1] + 1 else False for i in range(len(nums))]
        if False not in diffs:
            ans = len(nums)
        else:
            ans = diffs.index(False)

        ans = sum(nums[:ans])
        while ans in nums:
            ans += 1

        return ans
