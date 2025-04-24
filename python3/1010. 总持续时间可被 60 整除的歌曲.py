class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        ans = 0
        d = defaultdict(int)
        for v in time:
            vm = v % 60
            prevm = (60 - vm) % 60
            ans += d[prevm]
            d[vm] += 1

        return ans
