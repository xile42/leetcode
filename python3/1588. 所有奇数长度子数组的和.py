class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        acc = [0] + list(accumulate(arr))
        ans = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                ans += acc[j + 1] - acc[i]

        return ans
