class Solution:

    def decimalRepresentation(self, n: int) -> List[int]:

        ans = list()
        base = 1
        while n:
            cur = (n % 10) * base
            if cur:
                ans.append(cur)
            base *= 10
            n //= 10

        return ans[::-1]
