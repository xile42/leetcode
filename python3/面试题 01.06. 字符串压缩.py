class Solution:

    def compressString(self, S: str) -> str:

        ans = str()
        for c, ite in groupby(S):
            l = len(list(ite))
            ans += c + str(l)

        return ans if len(ans) < len(S) else S
