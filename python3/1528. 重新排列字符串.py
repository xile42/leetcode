class Solution:

    def restoreString(self, s: str, indices: List[int]) -> str:

        n = len(s)
        result = ["" for _ in range(n)]
        for i, v in enumerate(indices):
            result[v] = s[i]

        return "".join(result)
