class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0
        if all(v <= 1 for v in c.values()):
            return ans
        while nums:
            ans += 1
            for n in nums[:3]:
                c[n] -= 1
            nums = nums[3:]
            if all(v <= 1 for v in c.values()):
                return ans

        return ans
