class Solution:

    def countBadPairs(self, nums: List[int]) -> int:

        c = Counter()
        n = len(nums)
        ans = n * (n - 1) // 2
        for i, v in enumerate(nums):
            ans -= c[v - i]
            c[v - i] += 1

        return ans
