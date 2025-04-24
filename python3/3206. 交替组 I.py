class Solution:

    def numberOfAlternatingGroups(self, colors: List[int]) -> int:

        diffs = [colors[i] != colors[i + 1] for i in range(len(colors) - 1)]
        ans = sum(all(diffs[i:i+2]) for i in range(len(diffs) - 1))
        if colors[0] != colors[-1]:
            ans += sum([diffs[0], diffs[-1]])

        return ans
