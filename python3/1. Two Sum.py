class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_set = set()
        idx_map = dict()
        for idx, num in enumerate(nums):
            if target - num in nums_set:
                return [idx_map[target-num], idx]
            nums_set.add(num)
            idx_map[num] = idx
