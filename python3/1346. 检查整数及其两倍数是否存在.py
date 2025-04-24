class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:

        if Counter(arr)[0] > 1:
            return True

        s = set(arr)
        a = sorted(s)
        for n in a:
            if n * 2 in s and n:
                return True

        return False
