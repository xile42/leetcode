class Solution:

    def check(self, nums: List[int]) -> bool:

        cnt = 0
        for a, b in pairwise(nums):
            if a > b:
                cnt += 1

        return False if cnt > 1 else (True if cnt == 0 else (False if nums[0] < nums[-1] else True))
