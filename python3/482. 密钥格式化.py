class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:

        s = s.upper()
        s = "".join(s.split("-"))[::-1]
        results = list()
        idx = 0
        while idx < len(s):
            results.append(s[idx:idx+k])
            idx += k

        return "-".join(results)[::-1]
