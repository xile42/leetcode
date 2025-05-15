class Solution:

    def minSwaps(self, nums: List[int]) -> int:

        n = len(nums)
        ns = [[sum(map(int, str(nums[i]))), nums[i], i] for i in range(n)]
        ns.sort(key=lambda x: x[0:2])
        d = {i: ii for i, (_, _, ii) in enumerate(ns)}
        cnt = 0
        vis = [False] * n
        for cur in range(n):
            if vis[cur]:
                continue
            while not vis[cur]:
                vis[cur] = True
                cur = d[cur]
            cnt += 1

        return n - cnt
