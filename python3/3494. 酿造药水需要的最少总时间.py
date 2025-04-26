class Solution:

    def minTime(self, skill: List[int], mana: List[int]) -> int:

        n = len(skill)
        m = len(mana)

        ans = 0
        last = [-inf] * n
        last_offset = 0

        for bottle_idx in range(m):
            cur = 0  # 开始时间
            offset = 0  # 一圈跑下来，需要相对开始时间偏移多少
            finish_time_this_man = list()
            last_end = last_offset  # 前一个当前跑到哪
            for man_idx in range(n):
                last_end += last[man_idx]
                if cur < last_end:
                    offset += last_end - cur
                    cur = last_end
                finish_time_this_man.append(skill[man_idx] * mana[bottle_idx])
                cur += finish_time_this_man[-1]
            ans = max(ans, cur)
            last = finish_time_this_man
            last_offset = offset

        return ans
