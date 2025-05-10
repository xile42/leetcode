class Solution:

    def countOrders(self, n: int) -> int:

        base = pow(10, 9) + 7

        return (factorial(2 * n) // pow(2, n)) % base
