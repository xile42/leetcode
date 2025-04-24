class Solution:

    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)
        x, cnt = -1, 0
        for i in nums:
            if not cnt:
                x = i
            cnt += 1 if x == i else -1

        return x if cnt and nums.count(x) > n // 2 else -1
