class Solution:

    def checkDistances(self, s: str, distance: List[int]) -> bool:

        d = defaultdict(int)
        for i, c in enumerate(s):
            d[c] = i - d[c]

        for k, v in d.items():
            if v - 1 != distance[ord(k) - ord("a")]:
                return False

        return True
