class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:

        ck = nums.count(k)
        ans = ck
        for x in range(1, 50 + 1):
            left_cnt = 0
            this_ans = 1
            min_cnt = 0
            for num in nums:
                if num == x:
                    left_cnt += 1
                if num == k:
                    left_cnt -= 1
                min_cnt = min(min_cnt, left_cnt)
                this_ans = max(this_ans, left_cnt - min_cnt + ck)
            ans = max(ans, this_ans)

        return ans
