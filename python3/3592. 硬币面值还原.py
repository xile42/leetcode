class Solution:

    def findCoins(self, numWays: List[int]) -> List[int]:

        @cache
        def solve(tar, ns):

            if tar == 0:
                return 1

            if len(ns) == 0 or ns[0] > tar:
                return 0

            ans = 0
            for i in range(tar // ns[0] + 1):
                ans += solve(tar - ns[0] * i, tuple(ns[1:]))

            return ans

        ans = list()
        for i, v in enumerate(numWays):
            if v == 0:
                if solve(i + 1, tuple(ans)) != v:
                    return list()
                continue
            if solve(i + 1, tuple(ans)) != v:
                ans.append(i + 1)
                if solve(i + 1, tuple(ans)) != v:
                    return list()

        return ans
