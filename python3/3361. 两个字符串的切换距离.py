class Solution:

    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:

        ans = 0
        s_next = sum(nextCost)
        s_pre = sum(previousCost)
        pre_next = {i: v for i, v in enumerate(accumulate(nextCost))}
        pre_next[-1] = 0
        pre_pre = {i: v for i, v in enumerate(accumulate(previousCost))}
        pre_pre[-1] = 0
        for c1, c2 in zip(s, t):
            if c1 == c2:
                continue
            if c1 < c2:
                ans += min(
                    pre_next[ord(c2) - ord("a") - 1] - pre_next[ord(c1) - ord("a") - 1],
                    s_pre - (pre_pre[ord(c2) - ord("a")] - pre_pre[ord(c1) - ord("a")]),
                )
            else:
                ans += min(
                    s_next - (pre_next[ord(c1) - ord("a") - 1] - pre_next[ord(c2) - ord("a") - 1]),
                    pre_pre[ord(c1) - ord("a")] - pre_pre[ord(c2) - ord("a")],
                )

        return ans
