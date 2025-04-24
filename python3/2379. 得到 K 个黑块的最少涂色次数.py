class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:

        ns = [1 if c == "B" else 0 for c in blocks]
        left = 0
        cnt = sum(ns[:k])
        ans = min(k, k - cnt)
        for right in range(k, len(ns)):
            cnt += ns[right]
            cnt -= ns[left]
            left += 1
            ans = min(ans, k - cnt)

        return ans
