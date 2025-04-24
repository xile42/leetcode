class Solution:

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        ns = [[sum(mat[i]), i] for i in range(len(mat))]
        ns = sorted(ns)

        return [i[1] for i in ns[:k]]
