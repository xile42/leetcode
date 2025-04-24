class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:

        c = Counter()
        for i, n in enumerate(nums[::-1]):
            if n not in c:
                c[n] = i

        ans = -inf
        for i in range(1, k + 1):
            ans = max(ans, c[i] + 1)

        return ans
