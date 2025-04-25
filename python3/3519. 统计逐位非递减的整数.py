class Solution:

    def countNumbers(self, l: str, r: str, b: int) -> int:

        def to_b(x):

            if x == 0:
                return "0"
            ans = list()
            while x:
                r = x % b
                x //= b
                ans.append(str(r))

            return "".join(ans[::-1])

        low = list(map(int, to_b(int(l))))
        high = list(map(int, to_b(int(r))))
        n = len(high)
        diff_lh = n - len(low)  # 这样写无需给 low 补前导零，也无需 is_num 参数

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool, pre: int) -> int:

            if i == n:
                return 1

            lo = low[i - diff_lh] if limit_low and i >= diff_lh else 0
            hi = high[i] if limit_high else b - 1

            res = 0
            if limit_low and i < diff_lh:
                res += dfs(i + 1, True, False, 0)  # 什么也不填
                d = 1  # 下面循环从 1 开始
            else:
                d = lo
            # 枚举填数字 d
            for d in range(d, hi + 1):
                if d < pre:
                    continue
                res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi, d)

            return res

        return dfs(0, True, True, -9999) % 1_000_000_007
