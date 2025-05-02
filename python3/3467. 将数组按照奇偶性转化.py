class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = [1 if i & 1 else 0 for i in nums]
        return sorted(ans)