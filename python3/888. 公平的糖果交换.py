class Solution:

    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        n, m = sum(aliceSizes), sum(bobSizes)
        t = (n - m) // 2
        for j in bobSizes:
            if j + t in aliceSizes:
                return [j + t, j]
