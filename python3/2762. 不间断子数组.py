class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:

        c = Counter()
        ans = 0
        left = 0
        for right, v in enumerate(nums):
            c[v] += 1
            while len(c) > 3 or max(c.keys()) - min(c.keys()) > 2:
                c[nums[left]] -= 1
                if not c[nums[left]]:
                    del c[nums[left]]
                left += 1
            ans += right - left + 1

        return ans
