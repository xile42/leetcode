class Solution:

    def maximumSum(self, nums: List[int]) -> int:

        ans = -1
        d = dict()
        for v in nums:
            n = sum(map(int, str(v)))
            if n in d:
                ans = max(ans, v + d[n])
            if n not in d or d[n] < v:
                d[n] = v

        return ans
