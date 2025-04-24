class Solution:

    def halveArray(self, nums: List[int]) -> int:

        ans = 0
        tar = sum(nums) / 2
        nums = [-i for i in nums]
        heapify(nums)
        cur = 0

        while True:
            ans += 1
            v = -heappop(nums)
            cur += v / 2
            v /= 2
            heappush(nums, -v)
            if cur >= tar:
                break

        return ans
