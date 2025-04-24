class Solution:

    def countEven(self, num: int) -> int:

        count = 0
        for i in range(2, num + 1):
            if sum(map(int, list(str(i)))) & 1 == 0:
                count += 1

        return count
