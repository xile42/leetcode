class Solution:

    def numSplits(self, s: str) -> int:

        ans = 0
        right = Counter(s)
        left = Counter()

        for i, c in enumerate(s):

            left[c] += 1
            right[c] -= 1

            if right[c] == 0:
                del right[c]

            if len(left) == len(right):
                ans += 1

        return ans
