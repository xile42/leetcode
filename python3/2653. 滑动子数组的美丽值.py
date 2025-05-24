class Solution:

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        cnt = Counter()
        ans = [0] * (len(nums) - k + 1)
        for i, n in enumerate(nums):
            cnt[n] += 1
            if i >= k:
                cnt[nums[i - k]] -= 1
            if i >= k - 1:
                cur = 0
                for j in range(-50, 50 + 1):
                    cur += cnt[j]
                    if cur >= x:
                        ans[i - k + 1] = j if j < 0 else 0
                        break

        return ans
