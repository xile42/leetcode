class Solution:

    def destroyTargets(self, nums: List[int], space: int) -> int:

        c = Counter([i % space for i in nums])
        mx = max(c.values())
        nums.sort()
        for v in nums:
            if c[v % space] == mx:
                return v
