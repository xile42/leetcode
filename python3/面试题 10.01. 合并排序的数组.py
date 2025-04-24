class Solution:

    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """

        ans = list()
        i = j = 0
        while i < m or j < n:
            a = inf if i >= m else A[i]
            b = inf if j >= n else B[j]
            ans.append(min(a, b))
            if a < b:
                i += 1
            else:
                j += 1

        for i in range(m + n):
            A[i] = ans[i]
    
        return ans
