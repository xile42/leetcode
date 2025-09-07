class Solution:

    def sumDigitDifferences(self, nums: List[int]) -> int:

        c = defaultdict(lambda: defaultdict(int))
        for v in nums:
            i = 0
            while v:
                c[i][v % 10] += 1
                v //= 10
                i += 1

        n = len(nums)
        ans = 0
        for i in c:
            for v in c[i].values():
                ans += v * (n - v)

        return ans // 2
