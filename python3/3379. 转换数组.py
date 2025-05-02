class Solution:

    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [inf] * n
        for i, v in enumerate(nums):
            if v > 0:
                ans[i] = nums[(i + v) % n]
            elif v < 0:
                idx = i - abs(v)
                while not (0 <= idx < n):
                    idx += n
                ans[i] = nums[idx]
            else:
                ans[i] = nums[i]

        return ans
