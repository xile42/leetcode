class Solution:

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        base = 10 ** 9 + 7

        for l, r, k, v in queries:
            i = l
            while i <= r:
                nums[i] = (nums[i] * v) % base
                i += k

        ans = 0
        for v in nums:
            ans ^= v

        return ans
