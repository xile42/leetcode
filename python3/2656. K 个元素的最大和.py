class Solution:

    def maximizeSum(self, nums: List[int], k: int) -> int:

        mx = max(nums)
        ans = 0
        for _ in range(k):
            ans += mx
            mx += 1

        return ans
