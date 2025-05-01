class Solution:

    def numOfPairs(self, nums: List[str], target: str) -> int:

        cs = Counter(nums)
        ks = list(cs.keys())
        ans = 0
        for i, c in enumerate(ks):
            if c + c == target:
                ans += cs[c] * (cs[c] - 1)
            for j in range(i + 1, len(ks)):
                cc = ks[j]
                if c + cc == target:
                    ans += cs[c] * cs[cc]
                if cc + c == target:
                    ans += cs[c] * cs[cc]

        return ans
