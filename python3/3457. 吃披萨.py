class Solution:

    def maxWeight(self, pizzas: List[int]) -> int:

        raw_n = len(pizzas)
        pizzas.sort()
        ns = pizzas[raw_n // 2:]
        n = len(ns)
        t = n // 2
        if t & 1:
            odd = t // 2 + 1
            even = t
        else:
            odd = even = t // 2
        # print(n, t, odd, even)
        ans = 0
        ans += sum(ns[-odd:])
        ans += sum(ns[odd:-odd][::2])
        # print(ns[-odd:])
        # print(ns[odd:-odd], ns[odd:-odd][::2])
        return ans
