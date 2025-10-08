class Solution:

    def filterCharacters(self, s: str, k: int) -> str:

        cnt = Counter(s)
        ans = [c for c in s if cnt[c] < k]

        return "".join(ans)
