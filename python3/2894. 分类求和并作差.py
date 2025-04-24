class Solution:

    def differenceOfSums(self, n: int, m: int) -> int:

        num = n * (n + 1) // 2
        num1 = sum(i for i in range(1, n + 1) if i % m != 0)
        num2 = num - num1

        return num1 - num2
