class Solution:

    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        diff = [0] * (length + 1)
        for l, r, v in updates:
            diff[l] += v
            diff[r + 1] -= v
        acc = list(accumulate(diff))

        return acc[:-1]
