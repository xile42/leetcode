class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:

        d = defaultdict(int)
        d[0] = -1
        r = sum(nums) % p

        if r == 0:
            return 0

        ans = inf
        acc = 0
        for i, v in enumerate(nums):
            acc += v
            cur = acc % p
            tar = (cur - r) % p
            if tar in d:
                ans = min(ans, i - d[tar])
            d[cur] = i

        return ans if ans < inf and ans != len(nums) else -1
