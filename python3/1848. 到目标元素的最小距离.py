class Solution:

    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        ans = inf
        for i, n in enumerate(nums):
            if n == target:
                ans = min(ans, abs(i - start))

        return ans
