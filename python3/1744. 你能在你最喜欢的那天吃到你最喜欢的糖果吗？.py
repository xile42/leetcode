class Solution:

    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:

        acc = list(accumulate(candiesCount))
        ans = list()
        for t, d, c in queries:
            pre = 0 if t == 0 else acc[t - 1]
            s = ceil((pre + 1) / c)
            e = acc[t]
            ans.append(True if s - 1 <= d <= e - 1 else False)

        return ans