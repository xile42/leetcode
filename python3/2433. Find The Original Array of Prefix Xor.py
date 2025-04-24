class Solution:

    def findArray(self, pref: List[int]) -> List[int]:

        results = list()
        xor_value = 0
        for idx, num in enumerate(pref):
            xor_value = xor_value ^ num
            results.append(xor_value)
            xor_value = num

        return results
