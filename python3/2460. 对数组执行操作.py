class Solution:

    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        cnt = Counter(nums)[0]

        return [i for i in nums if i != 0] + [0] * cnt
            
