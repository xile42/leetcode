class Solution:

    def maxDistance(self, arrays: List[List[int]]) -> int:

        mx1, mx2 = -inf, -inf
        mxi = None
        mn1, mn2 = inf, inf
        mni = None
        for i, arr in enumerate(arrays):
            cur_mn, cur_mx = arr[0], arr[-1]

            if cur_mx > mx1:
                mx2 = mx1
                mx1 = cur_mx
                mxi = i
            elif cur_mx > mx2:
                mx2 = cur_mx
            
            if cur_mn < mn1:
                mn2 = mn1
                mn1 = cur_mn
                mni = i
            elif cur_mn < mn2:
                mn2 = cur_mn

        return abs(mx1 - mn1) if mxi != mni else max(abs(mx1 - mn2), abs(mx2 - mn1))
