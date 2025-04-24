class Solution:

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        ans = 0
        d = {0: -1}
        cur = 0
        for i, n in enumerate(nums):
            cur += n
            if cur - k in d:
                ans = max(ans, i - d[cur - k])
            if cur not in d:
                d[cur] = i

        return ans
