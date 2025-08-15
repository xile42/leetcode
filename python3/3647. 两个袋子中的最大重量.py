class Solution:

    def maxWeight(self, weights: List[int], w1: int, w2: int) -> int:

        s = set()
        s.add((w1, w2))
        for w in weights:
            to_add = set()
            for _w1, _w2 in s:
                if w <= _w1:
                    to_add.add((_w1 - w, _w2))
                if w <= _w2:
                    to_add.add((_w1, _w2 - w))
            s |= to_add

        return w1 + w2 - min(_w1 + _w2 for _w1, _w2 in s)

        # # 记忆化搜索，超时
        # n = len(weights)
        #
        # @cache
        # def f(i, w1, w2):
        #
        #     if i == n:
        #         return 0
        #
        #     cur = weights[i]
        #     cur_ans = 0
        #     if cur <= w1:
        #         cur_ans = max(cur_ans, f(i + 1, w1 - cur, w2) + cur)
        #     if cur <= w2:
        #         cur_ans = max(cur_ans, f(i + 1, w1, w2 - cur) + cur)
        #     cur_ans = max(cur_ans, f(i + 1, w1, w2))
        #
        #     return cur_ans
        #
        # ans = f(0, w1, w2)
        # f.cache_clear()
        #
        # return ans
