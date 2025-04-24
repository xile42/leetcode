class Solution:

    def findSubarrays(self, nums: List[int]) -> bool:

        s = set()
        cur = sum(nums[:2])
        s.add(cur)
        for idx in range(2, len(nums)):
            cur += nums[idx]
            cur -= nums[idx - 2]
            if cur in s:
                return True
            s.add(cur)

        return False
