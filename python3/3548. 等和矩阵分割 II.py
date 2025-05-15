class Solution:

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        m, n = len(grid), len(grid[0])

        rows = [sum(row) for row in grid]
        rows_s = [set(row) for row in grid]
        _all = sum(rows)

        # 行正序
        cur = 0
        s = set()
        for i in range(m - 1):  # 划分为[0:i] 和 [i + 1:]两部分
            cur += rows[i]
            # 情况1 直接两部分相等
            if cur == _all - cur:
                return True
            # 情况2 要忽视元素
            tar = cur - (_all - cur)
            if tar < 0:
                s |= rows_s[i]
                continue

            if i == 0:  # 不连通
                if tar == grid[0][0] or tar == grid[0][-1]:
                    return True
                s |= rows_s[i]
                continue
            if n == 1:  # 只能删0和i
                if tar in rows_s[0] | rows_s[i]:
                    return True
            else:
                if tar in s:
                    return True

            s |= rows_s[i]

        # 行逆序
        rows = rows[::-1]
        rows_s = rows_s[::-1]
        cur = 0
        s = set()
        for i in range(m - 1):  # 划分为[0:i] 和 [i + 1:]两部分
            cur += rows[i]
            # 情况1 直接两部分相等
            if cur == _all - cur:
                return True
            # 情况2 要忽视元素
            tar = cur - (_all - cur)
            if tar < 0:
                s |= rows_s[i]
                continue

            if i == 0:  # 不连通
                if tar == grid[-1][0] or tar == grid[-1][-1]:
                    return True
                s |= rows_s[i]
                continue
            if n == 1:  # 只能删0和i
                if tar in rows_s[0] | rows_s[i]:
                    return True
            else:
                if tar in s:
                    return True

            s |= rows_s[i]

        cols = [sum(row) for row in zip(*grid)]
        cols_s = [set(row) for row in zip(*grid)]

        # print("cols", cols)
        # print("cols_s", cols_s)

        # 列正序
        cur = 0
        s = set()
        for i in range(n - 1):  # 划分为[0:i] 和 [i + 1:]两部分
            cur += cols[i]
            # 情况1 直接两部分相等
            # print("col idx: {}, cur: {}".format(i, cur))
            if cur == _all - cur:
                return True
            # 情况2 要忽视元素
            tar = cur - (_all - cur)
            if tar < 0:
                s |= cols_s[i]
                continue
            # print("tar: {}".format(tar))
            if i == 0:  # 不连通
                if tar == grid[0][0] or tar == grid[-1][0]:
                    return True
                s |= cols_s[i]
                continue
            if m == 1:  # 只能删0和i
                if tar in cols_s[0] | cols_s[i]:
                    return True
            else:
                if tar in s:
                    return True

            s |= cols_s[i]

        # 列逆序
        cols = cols[::-1]
        cols_s = cols_s[::-1]
        cur = 0
        s = set()
        for i in range(n - 1):  # 划分为[0:i] 和 [i + 1:]两部分
            cur += cols[i]
            # print("col idx: {}, cur: {}".format(i, cur))
            # 情况1 直接两部分相等
            if cur == _all - cur:
                return True
            # 情况2 要忽视元素
            tar = cur - (_all - cur)
            if tar < 0:
                s |= cols_s[i]
                continue
            # print("tar: {}, s: {}".format(tar, s))
            if i == 0:  # 不连通
                if tar == grid[0][-1] or tar == grid[-1][-1]:
                    return True
                s |= cols_s[i]
                continue
            if m == 1:  # 只能删0和i
                if tar in cols_s[0] | cols_s[i]:
                    return True
            else:
                if tar in s:
                    return True

            s |= cols_s[i]

        return False
