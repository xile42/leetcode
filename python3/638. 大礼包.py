class Solution:

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:

        n = len(price)

        vs = list()
        for sp in special:
            if sum(sp[i] for i in range(n)) > 0 and sum(sp[i] * price[i] for i in range(n)) > sp[-1]:
                vs.append(sp)

        @cache
        def f(cur):

            min_price = sum(need * price[i] for i, need in enumerate(cur))
            for cs in vs:
                sp = cs[-1]
                next_needs = list()
                for i in range(n):
                    if cs[i] > cur[i]:
                        break
                    next_needs.append(cur[i] - cs[i])
                if len(next_needs) == n:
                    min_price = min(min_price, f(tuple(next_needs)) + sp)

            return min_price

        return f(tuple(needs))
