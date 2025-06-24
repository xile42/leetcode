class Solution:

    def minSwaps(self, nums: List[int]) -> int:

        odd_cnt = even_cnt = 0
        for v in nums:
            if v & 1:
                odd_cnt += 1
            else:
                even_cnt += 1

        if abs(odd_cnt - even_cnt) > 1:
            return -1

        def f(start, tar):

            ans = 0
            cur = start
            for i, v in enumerate(nums):
                if v & 1 == tar:
                    ans += abs(i - cur)
                    cur += 2

            return ans

        if odd_cnt == even_cnt:
            return min(f(0, 1), f(1, 1))

        tar = 1 if odd_cnt > even_cnt else 0
        return f(0, tar)
