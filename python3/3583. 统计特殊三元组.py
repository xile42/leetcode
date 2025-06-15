class Solution:

    def specialTriplets(self, nums: List[int]) -> int:

        mod = 10 ** 9 + 7
        c = Counter(nums)
        ans = 0
        left = Counter()
        n = len(nums)

        for i, v in enumerate(nums):
            if i == 0 or i == n - 1:
                left[v] += 1
                c[v] -= 1
                continue
            c[v] -= 1
            tar = v * 2
            ans += (left[tar] * c[tar]) % mod
            ans %= mod
            left[v] += 1

        return ans
