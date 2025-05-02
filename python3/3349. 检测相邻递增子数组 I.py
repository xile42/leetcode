class Solution:

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        def check(ns):
            for idx in range(1, len(ns)):
                if ns[idx] <= ns[idx - 1]:
                    return False
            return True

        n = len(nums)
        for l in range(n - 2 * k + 1):
            if check(nums[l:l+k]) and check(nums[l+k:l+2*k]):
                return True

        return False