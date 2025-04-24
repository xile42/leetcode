from math import lcm, gcd


class Solution:

    def maxScore(self, nums: List[int]) -> int:

        counter = Counter(nums)
        nums = list(set(nums))

        result = 0
        for idx in range(len(nums)):
            if counter[nums[idx]] > 1:
                continue
            new_nums = nums[:idx] + nums[idx+1:]
            result = max(lcm(*new_nums) * gcd(*new_nums), result)

        result = max(result, lcm(*nums) * gcd(*nums))

        return result

