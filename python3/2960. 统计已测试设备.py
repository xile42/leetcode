class Solution:

    def countTestedDevices(self, batteryPercentages: List[int]) -> int:

        cur = 0
        ans = 0
        for n in batteryPercentages:
            if n + cur > 0:
                ans += 1
                cur -= 1
            else:
                continue

        return ans
