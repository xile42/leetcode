class Solution:

    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pre = [0] * n
        s = set()
        for i in range(n):
            s.add(nums[i])
            pre[i] = len(s)
        suf = [0] * n
        s = set()
        for i in range(n - 1, -1, -1):
            s.add(nums[i])
            suf[i] = len(s)

        ans = list()
        for i in range(n):
            ans.append(pre[i] - (suf[i + 1] if i + 1 < n else 0))

        return ans
