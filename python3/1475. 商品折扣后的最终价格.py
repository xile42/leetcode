class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:

        d = {i: n for i, n in enumerate(prices)}
        s = list()
        for i, n in enumerate(prices):
            while len(s) and prices[s[-1]] >= n:
                t = s.pop(-1)
                d[t] = d[t] - n
            s.append(i)

        return [d[i] for i in range(len(prices))]
