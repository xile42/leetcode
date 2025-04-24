class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:

        s = sum(nums)
        nums.sort(reverse=True)
        cnt = len(nums)
        for v in nums:
            if cnt >= 3 and s - v and s - v > v:
                return s
            else:
                cnt -= 1
                s -= v

        return -1
