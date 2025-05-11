class Solution:

    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        ans = [0] * (n - k + 1)
        cnt = Counter()
        for i, v in enumerate(nums):
            cnt[v] += 1
            if i >= k:
                vv = nums[i - k]
                cnt[vv] -= 1
                if cnt[vv] == 0:
                    del cnt[vv]
            if i >= k - 1:
                ans[i - k + 1] = len(cnt)

        return ans
