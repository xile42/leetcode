class Solution:

    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:

        d = defaultdict(list)
        for div in divisors:
            ans = 0
            for n in nums:
                ans += n % div == 0
            d[ans].append(div)

        v = max(d.keys())

        return min(d[v])
