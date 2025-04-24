class Solution:

    def minimumPushes(self, word: str) -> int:

        l = len(set(word))
        n, r = divmod(l, 8)
        ans = 0
        ans += n * (n + 1) // 2 * 8
        ans += r * (n + 1)

        return ans
