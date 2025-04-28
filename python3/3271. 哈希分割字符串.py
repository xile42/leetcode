class Solution:

    def stringHash(self, s: str, k: int) -> str:

        parts = [s[i * k:(i + 1) * k] for i in range(len(s) // k)]
        ans = list()
        for part in parts:
            v = sum(ord(c) - ord("a") for c in part)
            ans.append(chr(v % 26 + ord("a")))

        return "".join(ans)
