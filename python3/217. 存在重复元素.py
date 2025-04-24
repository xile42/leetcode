class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:

        return any(v > 1 for v in Counter(nums).values())
        
