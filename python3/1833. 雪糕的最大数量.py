class Solution:

    def maxIceCream(self, costs: List[int], coins: int) -> int:

        acc = list(accumulate(sorted(costs)))
        ans = bisect_right(acc, coins)

        return ans
