class Solution:

    def customSortString(self, order: str, s: str) -> str:

        d = {c: i for i, c in enumerate(order)}

        return "".join(sorted(s, key=lambda x: d[x] if x in d else inf))
