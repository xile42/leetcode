class Solution:

    def countCompleteSubarrays(self, nums: List[int]) -> int:

        c = Counter()
        target = len(set(nums))
        ans = left = 0
        n = len(nums)
        for right in range(n):
            c[nums[right]] += 1
            while len(c) == target:
                c[nums[left]] -= 1
                if c[nums[left]] == 0:
                    del c[nums[left]]
                left += 1
            ans += left

        return ans
