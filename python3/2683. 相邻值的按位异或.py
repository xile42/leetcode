class Solution:

    def doesValidArrayExist(self, derived: List[int]) -> bool:

        def f(n):

            ans = list()
            ans.append(n)
            for v in derived[:-1]:
                ans.append(ans[-1] ^ v)

            return ans[-1] ^ ans[0] == derived[-1]

        return f(0) or f(1)
