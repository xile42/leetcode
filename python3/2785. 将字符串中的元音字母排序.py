class Solution:

    def sortVowels(self, s: str) -> str:

        ans = list(s)
        cs = sorted([c for c in s if c in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}])
        cur = 0
        for i, c in enumerate(s):
            if c in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}:
                ans[i] = cs[cur]
                cur += 1

        return "".join(ans)
