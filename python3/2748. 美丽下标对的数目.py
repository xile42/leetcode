class Solution:

    def countBeautifulPairs(self, nums: List[int]) -> int:

        ans = 0
        d = defaultdict(int)
        for v in nums:
            sv = str(v)
            c1 = sv[0]
            cn = sv[-1]
            for k, v in d.items():
                if gcd(int(k), int(cn)) == 1:
                    ans += v
            d[c1] += 1

        return ans
