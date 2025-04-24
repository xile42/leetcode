class Solution:

    def divisibleTripletCount(self, nums: List[int], d: int) -> int:

        n = len(nums)
        cnt = Counter()
        ans = 0
        for right in range(2, n):
            k = nums[right]
            j = nums[right - 1]
            for idx in range(right - 1):
                i = nums[idx]
                cnt[(i + j) % d] += 1
            ans += cnt[(d - (k % d)) % d]

        return ans
