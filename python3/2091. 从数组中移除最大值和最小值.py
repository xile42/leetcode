class Solution:

    def minimumDeletions(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)

        tar = set([max(nums), min(nums)])
        ns = [-1] + [i for i, n in enumerate(nums) if n in tar]

        ans = inf
        n = len(nums)
        ans = min(ans, ns[-1] + 1)
        for i, v in enumerate(ns):
            ans = min(ans, (v + 1 + n - ns[i + 1]) if i + 1 < len(ns) else inf)

        return ans
