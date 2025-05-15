class Solution:

    def minDeletion(self, s: str, k: int) -> int:

        c = Counter(s)
        cur = len(c)
        vs = sorted(c.values())
        ans = 0
        while cur > k:
            ans += vs.pop(0)
            cur -= 1

        return ans
