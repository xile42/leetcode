class Solution:

    def longestMountain(self, arr: List[int]) -> int:

        ns = [1 if arr[i] > arr[i - 1] else (-1 if arr[i] < arr[i - 1] else 0) for i in range(1, len(arr))]
        ans = 0
        pre = None
        prel = None
        for c, ite in groupby(ns):
            l = len(list(ite))
            if c == -1 and pre == 1:
                ans = max(ans, l + prel + 1)
            pre = c
            prel = l

        return ans
