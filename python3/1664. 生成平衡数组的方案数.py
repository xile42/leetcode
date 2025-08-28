class Solution:

    def waysToMakeFair(self, nums: List[int]) -> int:

        n = len(nums)
        a = [0] * n
        b = [0] * n
        ra = [0] * n
        rb = [0] * n

        for i in range(n):
            if i & 1:
                a[i] = a[i - 1]
                b[i] = b[i - 1] + nums[i]
            else:
                a[i] = a[i - 1] + nums[i]
                b[i] = b[i - 1] if i > 0 else 0

        for i in range(n - 1, -1, -1):
            if i & 1:
                ra[i] = ra[i + 1] if i < n - 1 else 0
                rb[i] = rb[i + 1] + nums[i] if i < n - 1 else nums[i]
            else:
                ra[i] = ra[i + 1] + nums[i] if i < n - 1 else nums[i]
                rb[i] = rb[i + 1] if i < n - 1 else 0

        ans = 0
        for i in range(n):
            left_a = a[i - 1] if i > 0 else 0
            left_b = b[i - 1] if i > 0 else 0
            right_a = ra[i + 1] if i < n - 1 else 0
            right_b = rb[i + 1] if i < n - 1 else 0
            if left_a + right_b == left_b + right_a:
                ans += 1

        return ans
