class Solution:

    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        ans = 0
        cur = sum(calories[:k])
        if cur < lower:
            ans -= 1
        elif cur > upper:
            ans += 1
        for i in range(k, len(calories)):
            cur += calories[i]
            cur -= calories[i - k]
            if cur < lower:
                ans -= 1
            elif cur > upper:
                ans += 1

        return ans
