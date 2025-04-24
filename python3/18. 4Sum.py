class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)
        results = list()
        length = len(nums)
        for idx in range(length-3):
            for jdx in range(idx+1, length-2):
                new_target = target - nums[idx] - nums[jdx]
                left = jdx + 1
                right = length - 1
                while left < right:
                    diff = new_target - nums[left] - nums[right]
                    if diff == 0 and [nums[idx], nums[jdx], nums[left], nums[right]] not in results:
                        results.append([nums[idx], nums[jdx], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif diff > 0:
                        left += 1
                    else:
                        right -= 1

        return results
