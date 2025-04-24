class Solution:

    def countNicePairs(self, nums: List[int]) -> int:

        cnt = Counter()
        ans = 0
        base = pow(10, 9) + 7
        for i in range(len(nums)):
            cur = nums[i] - int(str(nums[i])[::-1])
            ans += cnt[cur]
            ans %= base
            cnt[cur] += 1

        return ans
