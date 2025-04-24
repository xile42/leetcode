class Solution:

    def findLHS(self, nums: List[int]) -> int:

        c = Counter(nums)
        ans = 0
        for n in nums:
            if n + 1 not in c:
                continue
            ans = max(ans, c[n] + c[n + 1])

        return ans
