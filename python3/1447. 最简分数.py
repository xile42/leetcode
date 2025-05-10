class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:

        ans = set()
        for q in range(2, n + 1):
            for p in range(1, q):
                if gcd(p, q) == 1:
                    ans.add("{}/{}".format(p, q))

        return list(ans)
