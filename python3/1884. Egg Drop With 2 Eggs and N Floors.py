class Solution:

    def twoEggDrop(self, n: int) -> int:

        i = 1
        count = 0
        while n > 0:
            n -= i
            i += 1
            count += 1

        return count
