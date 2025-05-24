class Solution:

    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:

        n = len(arr)
        vis = [False] * n
        d = defaultdict(list)
        for i in range(k):
            if vis[i]:
                continue
            j = i
            while j < n:
                if vis[j]:
                    break
                vis[j] = True
                d[i].append(arr[j])
                j = (j + k) % n

        ans = 0
        for vs in d.values():
            vs.sort()
            l = len(vs)
            mid = vs[l // 2]
            ans += sum([abs(v - mid) for v in vs])

        return ans
