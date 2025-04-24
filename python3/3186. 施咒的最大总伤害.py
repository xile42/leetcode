class Solution:

    def maximumTotalDamage(self, power: List[int]) -> int:

        counter = Counter(power)
        v = dict()
        for key, value in counter.items():
            v[key] = key * value
        power = sorted(set(power))
        dp = [0, v[power[0]]]
        for i in range(2, len(power)+1):
            if i - 3 >= 0 and power[i-1] - power[i-3] <= 2:
                pre = dp[i-3]
            elif i - 2 >= 0 and power[i-1] - power[i-2] <= 2:
                pre = dp[i-2]
            else:
                pre = dp[i-1]
            dp.append(max(v[power[i-1]] + pre, dp[-1]))

        return dp[-1]
