class Solution:

    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums) != 1:
            new = list()
            for i in range(len(nums) // 2):
                if i & 1:
                    new.append(max(nums[2 * i], nums[2 * i + 1]))
                else:
                    new.append(min(nums[2 * i], nums[2 * i + 1]))
            nums = new

        return nums[0]
