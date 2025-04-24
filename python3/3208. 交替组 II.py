class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        n = len(colors)
        colors += colors
        diffs = "".join(["t" if colors[idx] != colors[idx + 1] else "f" for idx in range(len(colors) - 1)])
        ans = 0
        for c, ite in groupby(diffs[:n + k - 2]):
            if c == "f":
                continue
            l = len(list(ite))
            ans += max(l - (k - 1) + 1, 0)

        return ans
