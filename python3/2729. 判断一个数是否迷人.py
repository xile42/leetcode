class Solution:

    def isFascinating(self, n: int) -> bool:

        c = Counter(str(n)) + Counter(str(n * 2)) + Counter(str(n * 3))

        return True if all(c[str(i)] == 1 for i in range(1, 10)) and c["0"] == 0 else False
