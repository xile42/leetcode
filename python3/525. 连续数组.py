class Solution:

    def findMaxLength(self, nums: List[int]) -> int:

        cur = 0
        cnt = Counter()
        cnt[0] = -1
        ans = 0
        for i, n in enumerate(nums):
            update = 1 if n == 1 else -1
            cur += update
            if cur in cnt:
                ans = max(ans, i - cnt[cur])
            else:
                cnt[cur] = i

        return ans
