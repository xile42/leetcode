class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        ans = 0
        s = 0
        cnt = Counter()
        for i, n in enumerate(nums):
            s += n
            cnt[n] += 1
            if i >= k:
                v = nums[i - k]
                s -= v
                cnt[v] -= 1
                if cnt[v] == 0:
                    del cnt[v]
            if i >= k - 1 and len(cnt) == k:
                ans = max(ans, s)

        return ans
