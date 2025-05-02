from typing import List


class Solution:

    def separateSquares(self, squares: List[List[int]]) -> float:

        ns = [[i[1], i[1] + i[2], i[2] ** 2] for i in squares]
        tar = sum([i[-1] for i in ns]) / 2
        e = 1e-5
        # print(tar)

        def check(v):

            ans = 0
            for s, e, m in ns:
                if e <= v:
                    ans += m
                    continue
                if s >= v:
                    continue
                ans += (e - s) * (v - s)

            return ans

        left = 0
        right = 2 * 10 ** 9 + 2
        while left <= right and right - left > e:
            mid = left + (right - left) / 2
            v = check(mid)
            # err = v - tar
            # print(left, right, mid, v, err)
            # if abs(err) <= e:
            # if v == tar:
            #     if right == mid:
            #         print("???", right, mid)
            #         break
            #     right = mid
            if v >= tar:
                if right == mid:
                    # print("???2", right, mid)
                    break
                right = mid
            else:
                if left == mid:
                    # print("???3", right, mid)
                    break
                left = mid

            # print(left, right, left <= right, right - left > 1e-20)

        return left


foo = Solution()
foo.separateSquares([[0,0,1],[2,2,1]])

