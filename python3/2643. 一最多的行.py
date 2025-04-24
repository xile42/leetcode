class Solution:

    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        ns = [[sum(row), i] for i, row in enumerate(mat)]
        ns = sorted(ns, key=lambda x: x[0], reverse=True)

        return ns[0][::-1]
