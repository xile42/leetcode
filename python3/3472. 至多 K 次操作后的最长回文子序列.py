class Solution:

    def longestPalindromicSubsequence(self, s: str, k: int) -> int:

        @cache
        def dist(a, b):

            if ord(a) > ord(b):
                a, b = b, a

            return min((ord(b) - ord(a)) % 26, (ord(a) + 26 - ord(b)) % 26)

        @cache
        def dfs(i: int, j: int, chance: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            ans = list()
            if s[i] == s[j]:
                ans.append(dfs(i + 1, j - 1, chance) + 2)
            else:
                ans.append(dfs(i + 1, j, chance))
                ans.append(dfs(i, j - 1, chance))

            d = dist(s[i], s[j])
            # print("{}, {}, dist {}".format(s[i], s[j], d))
            if d <= chance:
                ans.append(dfs(i + 1, j - 1, chance - d) + 2)

            # print("dfs({}, {}, {}), {}".format(i, j, chance, max(ans)))
            return max(ans)

        return dfs(0, len(s) - 1, k)