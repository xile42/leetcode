import numpy as np


class Solution:

    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original) != m * n:
            return list()

        result = np.array(original).reshape((m, n)).tolist()
        return result
