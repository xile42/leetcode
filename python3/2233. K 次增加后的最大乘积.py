class Solution:

    def maximumProduct(self, nums: List[int], k: int) -> int:

        heapify(nums)
        for _ in range(k):
            val = heappop(nums)
            heappush(nums, val + 1)

        ans = 1
        base = 10 ** 9 + 7
        for v in nums:
            ans *= v
            ans %= base

        return ans
