class Solution:

    def getNoZeroIntegers(self, n: int) -> List[int]:

        for i in count(1):
            j = n - i
            if "0" not in str(i) and "0" not in str(j):
                return[i, j]
