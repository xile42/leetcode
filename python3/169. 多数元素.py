class Solution:

    def majorityElement(self, nums: List[int]) -> int:

        return sorted(Counter(nums).items(), key=lambda x: x[-1], reverse=True)[0][0]
        
