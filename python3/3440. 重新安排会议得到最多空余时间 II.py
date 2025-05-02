from collections import defaultdict


class Solution:

    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:

        n = len(startTime)
        blanks = list()
        for i, (s, e) in enumerate(zip(startTime, endTime)):

            if i == 0 and s != 0:
                blanks.append(s)
            else:
                v = s - endTime[i - 1]
                if v:
                    blanks.append(s - endTime[i - 1])
        if endTime[n - 1] != eventTime:
            blanks.append(eventTime - endTime[n - 1])

        blanks.sort()
        # print(blanks)
        ans = blanks[-1]
        for i, (s, e) in enumerate(zip(startTime, endTime)):
            left_max = 0 if i == 0 else endTime[i - 1]
            right_max = eventTime if i == n - 1 else startTime[i + 1]
            ans1 = (right_max - left_max) - (e - s)

            left_blank = s - left_max
            right_blank = right_max - e
            cnt = defaultdict(int)
            cnt[left_blank] += 1
            cnt[right_blank] += 1
            need = e - s
            ans2 = 0
            for j in range(len(blanks) - 1, -1, -1):
                v = blanks[j]
                if cnt[v]:
                    cnt[v] -= 1
                    continue
                if v < need:
                    break
                ans2 = right_max - left_max
                break
            # print("i {}, ans1 {}, ans2 {}, left_max {}, right_max {}".format(i, ans1, ans2, left_max, right_max))
            this_ans = max(ans1, ans2)
            ans = max(ans, this_ans)

        return ans
