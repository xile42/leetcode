class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)
        acc = list(accumulate(nums))
        cnt = Counter()
        cnt[0] = 1
        ans = 0
        for i in range(n):
            ans += cnt[acc[i] % k]
            cnt[acc[i] % k] += 1

        return ans
