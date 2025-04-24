class Solution:

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        ns = list()
        for a, b in dimensions:
            ns.append([sqrt(a ** 2 + b ** 2), a * b])
        ns.sort()

        return ns[-1][-1]
