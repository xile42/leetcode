class Solution:

    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        cur = set(mat[0])
        for i in range(1, len(mat)):
            cur &= set(mat[i])

        return -1 if not cur else min(cur)
