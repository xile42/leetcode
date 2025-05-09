class Solution:

    def minSwaps(self, data: List[int]) -> int:

        k = sum(data)
        ans = inf
        s = 0
        for i, n in enumerate(data):
            s += n
            if i >= k:
                s -= data[i - k]
            if i >= k - 1:
                ans = min(ans, k - s)

        return ans
