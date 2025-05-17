class Solution:

    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:

        bc = Counter(birth)
        dc = Counter(death)
        keys = sorted(bc.keys() | dc.keys())

        cur = 0
        mx = -inf
        ans = None
        for t in keys:
            cur += bc[t]
            if cur > mx:
                mx = cur
                ans = t
            cur -= dc[t]

        return ans
