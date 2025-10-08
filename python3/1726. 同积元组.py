class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:

        c = Counter()
        n = len(nums)

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                tar = nums[i] * nums[j]
                ans += c[tar] * 8
                c[tar] += 1

        return ans
