class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        ns = list()
        ns.append([0, 0])
        mx = -inf
        for d, p in sorted(zip(difficulty, profit), key=lambda x: x[0]):
            mx = max(mx, p)
            ns.append([d, mx])

        n = len(ns)
        ans = 0
        i = 0
        for w in sorted(worker):
            while i + 1 < n and ns[i + 1][0] <= w:
                i += 1
            ans += ns[i][-1]

        return ans
