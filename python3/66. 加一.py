class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:

        d = int("".join(map(str, digits)))
        d += 1
        result = list(map(int, list(str(d))))

        return result
