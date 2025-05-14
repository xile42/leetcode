class Solution:

    def incremovableSubarrayCount(self, nums: List[int]) -> int:

        def check(arr):

            if not arr or all(b - a > 0 for a, b in pairwise(arr)):
                return True

            return False

        n = len(nums)
        idxs = list(range(n))
        ans = 0
        for i in range(n):
            for j in range(i, n):
                arr = nums[:i] + nums[j + 1:]
                if check(arr):
                    ans += 1

        return ans
