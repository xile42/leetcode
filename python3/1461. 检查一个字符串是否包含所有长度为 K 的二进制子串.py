class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:

        hash = set()
        for i in range(k, len(s) + 1):
            hash.add(s[i - k:i])

        return len(hash) == 2 ** k
