class Solution:

    def minimumDifference(self, nums: List[int], k: int) -> int:

        sn = sorted(nums)
        ans = inf
        for s in range(len(nums)):
            e = s + k - 1
            if e >= len(nums):
                break
            ans = min(ans, sn[e] - sn[s])

        return ans
