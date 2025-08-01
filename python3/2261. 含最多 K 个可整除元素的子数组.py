class Solution:

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:

        ns = [1 if n % p == 0 else 0 for n in nums]
        n = len(nums)
        acc = list(accumulate(ns))

        ans = set()
        for i in range(n):
            for j in range(i, n):
                if acc[j] - (acc[i - 1] if i > 0 else 0) <= k:
                    ans.add(tuple(nums[i:j + 1]))

        return len(ans)
