class Solution:

    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        import numpy as np

        return np.matmul(np.array(mat1), np.array(mat2)).tolist()
