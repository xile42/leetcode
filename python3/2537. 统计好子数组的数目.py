class Solution:

    def countGood(self, nums: List[int], k: int) -> int:

        c = Counter()
        ans = left = 0
        n = len(nums)
        cur = 0
        for right in range(n):
            c[nums[right]] += 1
            cur += c[nums[right]] - 1
            while cur >= k:
                c[nums[left]] -= 1
                cur -= c[nums[left]]
                left += 1
            ans += left

        return ans
