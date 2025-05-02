class Solution:

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        def solve(eventTime, k, startTime, endTime):

            left = ans = 0
            n = len(startTime)
            sem = list()
            for i, (s, e) in enumerate(zip(startTime, endTime)):
                if i == 0:
                    sem.append([s, e, int(s != 0)])  # need move: 1 else: 0
                else:
                    sem.append([s, e, int(s != endTime[i - 1])])  # need move: 1 else: 0

            ans = 0
            cur = 0  # total time used
            cnt = 0
            used = 0
            used_map = dict()
            for right, (s, e, m) in enumerate(sem):

                cur += e - s
                cnt += m
                used += 1 if cnt > 0 else 0
                used_map[right] = 1 if cnt > 0 else 0
                # print("after in, right {}, left {}, cur {}, used {}, cnt {}".format(right, left, cur, used, cnt))
                while used > k:
                    ss, ee, mm = sem[left]
                    cur -= ee - ss
                    used -= used_map[left]
                    cnt -= mm
                    left += 1
                # print("after out, right {}, left {}, cur {}, used {}, cnt {}".format(right, left, cur, used, cnt))
                cur_left_max = 0 if left == 0 else sem[left - 1][1]
                cur_right_max = eventTime if right == n - 1 else sem[right + 1][0]
                this_ans = (cur_right_max - cur_left_max) - cur
                # print("this_ans", this_ans)
                ans = max(ans, this_ans)

            return ans

        ans = solve(eventTime, k, startTime, endTime)

        return ans
