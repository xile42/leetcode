class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pre = [1] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i]

        suf = [1] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i]

        ans = list()
        for i in range(n):
            left = 1 if i == 0 else pre[i - 1]
            right = 1 if i == n - 1 else suf[i + 1]
            ans.append(left * right)

        return ans
