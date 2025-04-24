import string


class Solution:

    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        d = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}
        for c, v in zip(chars, vals):
            d[c] = v
        ns = [d[c] for c in s]
        for i in range(1, len(ns)):
            ns[i] = max(ns[i], ns[i - 1] + ns[i])

        return max(max(ns), 0)
