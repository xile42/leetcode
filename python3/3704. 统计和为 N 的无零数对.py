class Solution:

    def countNoZeroPairs(self, n: int) -> int:

        s = list(map(int, str(n)))[::-1]
        n = len(s)

        @cache
        def dfs(i, c, valid_a, valid_b, first):

            if i == n:
                return 1 if c == 0 else 0

            if i == n - 1 and c == s[i]:
                return 1

            a_range = range(1, 10) if first else (range(0, 10) if valid_a else [0])
            b_range = range(1, 10) if first else (range(0, 10) if valid_b else [0])

            ans = 0
            for a in a_range:
                for b in b_range:
                    total = a + b + c
                    cur = total % 10
                    if cur != s[i]:
                        continue
                    new_c = total // 10
                    new_valid_a = valid_a and (a != 0)
                    new_valid_b = valid_b and (b != 0)
                    ans += dfs(i + 1, new_c, new_valid_a, new_valid_b, False)

            return ans

        ans = dfs(0, 0, True, True, True)
        dfs.cache_clear()

        return ans
