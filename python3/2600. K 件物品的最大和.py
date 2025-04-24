class Solution:

    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        ans = 0
        ans += min(numOnes, k)
        k -= min(numOnes, k)
        k -= min(numZeros, k)
        ans -= min(numNegOnes, k)

        return ans
