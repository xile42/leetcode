class Solution:

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        ns = list()
        i = 0
        while n:
            if n & 1:
                ns.append(i)
            n >>= 1
            i += 1

        acc = [0] + list(accumulate(ns))

        ans = list()
        base = 10 ** 9 + 7
        for l, r in queries:
            ans.append(pow(2, acc[r + 1] - acc[l], base))

        return ans
