class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:

##        n = len(ages)
##        ans = 0
##        for i in range(n):
##            for j in range(i + 1, n):
##                if not (ages[j] <= 0.5 * ages[i] + 7 or ages[j] > ages[i] or (ages[j] > 100 and ages[i] < 100)):
##                    ans += 1
##                if not (ages[i] <= 0.5 * ages[j] + 7 or ages[i] > ages[j] or (ages[i] > 100 and ages[j] < 100)):
##                    ans += 1
##
##        return ans

        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1

        ans = cnt_window = age_y = 0
        for age_x, c in enumerate(cnt):
            cnt_window += c
            if age_y * 2 <= age_x + 14:  # 不能发送好友请求
                cnt_window -= cnt[age_y]
                age_y += 1
            if cnt_window:  # 存在可以发送好友请求的用户
                ans += c * cnt_window - c
        return ans

