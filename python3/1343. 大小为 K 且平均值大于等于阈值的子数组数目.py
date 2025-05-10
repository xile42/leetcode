class Solution:

    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        tar = threshold * k
        ans = 0
        s = 0
        for i, n in enumerate(arr):
            s += n
            if i >= k:
                s -= arr[i - k]
            if i >= k - 1:
                ans += 1 if s >= tar else 0

        return ans
