class Solution:

    def maxKelements(self, nums: List[int], k: int) -> int:

        ans = 0
        nums = [-i for i in nums]
        heapify(nums)
        for _ in range(k):
            v = -heappop(nums)
            ans += v
            heappush(nums, -ceil(v / 3))

        return ans
