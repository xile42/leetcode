class Solution:

    def trimMean(self, arr: List[int]) -> float:

        n = len(arr)
        k = int(n * 0.05)

        return sum(sorted(arr)[k:-k]) / (n - 2 * k)
