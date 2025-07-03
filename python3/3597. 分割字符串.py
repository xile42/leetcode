class Solution:

    def partitionString(self, s: str) -> List[str]:

        vis = set()
        ans = list()
        start = end = 0
        while end < len(s):
            ss = s[start:end + 1]
            if ss not in vis:
                ans.append(ss)
                vis.add(ss)
                start = end + 1
            end += 1

        return ans
