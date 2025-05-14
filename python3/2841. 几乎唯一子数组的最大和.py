class Solution:

    def maxSum(self, nums: List[int], m: int, k: int) -> int:

        ans = 0
        s = 0
        cnt = Counter()
        for i, n in enumerate(nums):
            s += n
            cnt[n] += 1
            if i >= k:
                s -= nums[i - k]
                cnt[nums[i - k]] -= 1
                if cnt[nums[i - k]] == 0:
                    del cnt[nums[i - k]]
            if i >= k - 1 and len(cnt) >= m:
                ans = max(ans, s)

        return ans
