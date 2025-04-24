class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:

        c = Counter(arr)
        u = [w for w in arr if c[w] == 1]

        return "" if k - 1 >= len(u) else u[k - 1]
