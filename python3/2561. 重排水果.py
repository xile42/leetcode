class Solution:

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        cnt = defaultdict(int)
        for x, y in zip(basket1, basket2):
            cnt[x] += 1
            cnt[y] -= 1  # 交集元素互相抵消

        a, b = [], []
        for x, c in cnt.items():
            if c % 2:  # 奇数无法均分
                return -1
            # 剩余元素的一半放入 a 或者 b
            if c > 0:
                a.extend([x] * (c // 2))
            else:
                b.extend([x] * (-c // 2))

        a.sort()
        b.sort(reverse=True)
        mn = min(cnt)  # 中介

        return sum(min(x, y, mn * 2) for x, y in zip(a, b))
