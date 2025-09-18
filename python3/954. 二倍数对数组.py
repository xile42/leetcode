class Solution:

    def canReorderDoubled(self, arr: List[int]) -> bool:

        c = Counter(arr)
        arr.sort(key=abs)
        n = len(arr)

        for v in arr:

            if v not in c:
                continue

            c[v] -= 1
            c[v * 2] -= 1
            if c[v] < 0 or c[v * 2] < 0:
                return False
            if c[v] == 0:
                del c[v]
            if c[v * 2] == 0:
                del c[v * 2]

        return len(c) == 0
