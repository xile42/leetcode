class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        idx = 0
        min_result = float("inf")
        min_diff = float("inf")

        while idx < len(nums) - 2:
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[idx] + nums[left] + nums[right] - target
                if current_sum == 0:
                    return target
                elif abs(current_sum) < min_diff:
                    min_result = current_sum + target
                    min_diff = abs(current_sum)
                if current_sum < 0:
                    left += 1
                else:
                    right -= 1

            idx += 1

        return min_result
