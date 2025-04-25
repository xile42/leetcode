class Solution:

    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        ans = 0
        ns = [1 if n % modulo == k else 0 for n in nums]
        acc = list(accumulate(ns))
        c = Counter()
        c[0] = 1
        for i in range(len(acc)):
            ans += c[(acc[i] - k) % modulo]
            c[acc[i] % modulo] += 1

        return ans
