class Solution:

    def maximumGroups(self, grades: List[int]) -> int:

        ans = 1
        grades.sort()
        pre = grades[0]
        cnt = 1
        cur = 0
        cur_cnt = 0
        for i, n in enumerate(grades):
            if i == 0:
                continue
            cur += n
            cur_cnt += 1
            if cur > pre and cur_cnt > cnt:
                ans += 1
                pre = cur
                cnt = cur_cnt
                cur = 0
                cur_cnt = 0

        return ans
