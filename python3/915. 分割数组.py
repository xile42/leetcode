class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:

        n = len(nums)

        pre = [-inf] * n
        for i in range(n):
            if i == 0:
                pre[i] = nums[i]
            else:
                pre[i] = max(pre[i - 1], nums[i])

        suf = [inf] * n
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                suf[i] = nums[i]
            else:
                suf[i] = min(suf[i + 1], nums[i])

        for i in range(1, n):
            if pre[i - 1] <= suf[i]:
                return i
