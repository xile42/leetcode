class Solution:

    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        ans = list()
        s, e = toBeRemoved
        for ss, ee in intervals:
            if ee <= s or ss >= e:
                ans.append([ss, ee])
            else:
                if ss < s:
                    ans.append([ss, s])
                if ee > e:
                    ans.append([e, ee])

        return ans
