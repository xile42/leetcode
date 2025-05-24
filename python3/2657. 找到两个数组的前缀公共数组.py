class Solution:

    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        cura, curb = 0, 0
        ans = list()
        for a, b in zip(A, B):
            cura |= 1 << a
            curb |= 1 << b
            ans.append((cura & curb).bit_count())

        return ans
