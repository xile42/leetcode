class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        results = list()
        results_set = set()

        idx = 0
        while idx < len(nums) - 2:
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[idx] + nums[left] + nums[right]
                if current_sum == 0:
                    if (nums[idx], nums[left], nums[right]) not in results_set:
                        results.append([nums[idx], nums[left], nums[right]])
                        results_set.add((nums[idx], nums[left], nums[right]))
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    left += 1

            idx += 1

        return results
