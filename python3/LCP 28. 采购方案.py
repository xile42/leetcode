class Solution:

    def purchasePlans(self, nums: List[int], target: int) -> int:

        sn = sorted(nums)
        base = 1000000007
        ans = left = 0
        right = len(sn) - 1
        while left < right:
            if sn[left] + sn[right] <= target:
                ans += (right - left) % base
                left += 1
            else:
                right -= 1

        return ans % base
