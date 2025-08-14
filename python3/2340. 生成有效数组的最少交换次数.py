class Solution:

    def minimumSwaps(self, nums: List[int]) -> int:

        n = len(nums)
        mx, mn = max(nums), min(nums)
        i = 0
        while nums[i] != mn:
            i += 1
        j = n - 1
        while nums[j] != mx:
            j -= 1

        ans = n - 1 - j + i
        ans -= 1 if i > j else 0

        return ans
