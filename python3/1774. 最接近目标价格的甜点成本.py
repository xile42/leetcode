class Solution:

    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        @cache
        def f(cur, tar):

            if tar == 0 or cur >= len(toppingCosts):
                return 0

            ans = -inf
            for i in range(3):
                v = f(cur + 1, tar - i * toppingCosts[cur]) + i * toppingCosts[cur]
                if abs(v - tar) < abs(ans - tar) or (abs(v - tar) == abs(ans - tar) and v < ans):
                    ans = v

            return ans

        ans = -inf
        for base in baseCosts:
            topping = f(0, target - base)
            total = base + topping
            if abs(total - target) < abs(ans - target) or (abs(total - target) == abs(ans - target) and total < ans):
                ans = total

        f.cache_clear()

        return ans
