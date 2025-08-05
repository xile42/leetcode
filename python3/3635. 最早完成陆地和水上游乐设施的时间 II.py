class Solution:

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        a = sorted(zip(landStartTime, landDuration), key=lambda x: x[0] + x[1])
        b = sorted(zip(waterStartTime, waterDuration), key=lambda x: x[0] + x[1])

        ans1 = inf
        cur = a[0][0] + a[0][1]
        for s, d in b:
            if s <= cur:
                ans1 = min(ans1, cur + d)
            else:
                ans1 = min(ans1, s + d)

        ans2 = inf
        cur = b[0][0] + b[0][1]
        for s, d in a:
            if s <= cur:
                ans2 = min(ans2, cur + d)
            else:
                ans2 = min(ans2, s + d)

        return min(ans1, ans2)
