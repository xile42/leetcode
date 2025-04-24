class Solution:

    def maxPower(self, s: str) -> int:

        st = list()
        cnt = 1
        t_cnt = 0
        for c in s:
            if not st or st[-1] != c:
                st.append(c)
                if t_cnt != 0:
                    cnt = max(cnt, t_cnt + 1)
                    t_cnt = 0
            else:
                t_cnt += 1

        if t_cnt != 0:
            cnt = max(cnt, t_cnt + 1)

        return cnt
