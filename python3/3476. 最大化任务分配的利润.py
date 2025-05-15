class Solution:

    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:

        c = Counter(workers)
        tasks.sort(reverse=True, key=lambda x: x[-1])

        ans = 0
        used = False
        for k, v in tasks:
            if c[k]:
                ans += v
                c[k] -= 1
            elif not used:
                ans += v
                used = True

        return ans
