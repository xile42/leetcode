class Solution:

    def minimumBuckets(self, hamsters: str) -> int:

        if "H" not in hamsters:
            return 0

        ans = 0
        n = len(hamsters)
        d = defaultdict(bool)
        for i, c in enumerate(hamsters):
            if c == ".":
                continue
            if i - 1 >= 0 and d[i - 1]:
                continue
            if i + 1 < n and hamsters[i + 1] == ".":
                ans += 1
                d[i + 1] = True
            else:
                if i - 1 < 0 or hamsters[i - 1] == "H":
                    return -1
                else:
                    ans += 1
                    d[i - 1] = True

        return ans
