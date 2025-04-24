class Solution:

    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        ans = left = 0
        cnt = Counter()
        for right, n in enumerate(nums):
            cnt[n] += 1
            while len(cnt) != right - left + 1:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans = max(ans, sum(cnt.keys()))

        return ans
