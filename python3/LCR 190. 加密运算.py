class Solution:

    def encryptionCalculate(self, dataA: int, dataB: int) -> int:

        return reduce(add, [dataA, dataB])
