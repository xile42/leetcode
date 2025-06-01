class Solution:

    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        ans = 0
        meetings.sort(key=lambda x: x[0])
        s, e = meetings[0]
        for i in range(1, len(meetings)):
            ss, ee = meetings[i]
            if ss <= e:
                s, e = s, max(e, ee)
            else:
                ans += e - s + 1
                s, e = ss, ee

        ans += e - s + 1

        return days - ans
