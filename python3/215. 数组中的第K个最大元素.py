class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:

        h = list()
        for n in nums:
            if len(h) < k:
                heappush(h, n)
                continue
            if n > h[0]:
                heappush(h, n)
                heappop(h)

        return h[0]
