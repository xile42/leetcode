class Solution:

    def numTimesAllBlue(self, flips: List[int]) -> int:

        ans = 0
        i = 0
        j = -inf
        n = len(flips)
        ns = [0] * n
        for idx in flips:
            ns[idx - 1] = 1
            while i < n and ns[i] == 1:
                i += 1
            j = max(j, idx - 1)
            if i - 1 == j:
                ans += 1

        return ans
