class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        h = set()
        left = 0
        ans = set()
        for right in range(10, len(s) + 1):
            ss = s[left:right]
            if ss in h:
                ans.add(ss)
            h.add(ss)
            left += 1

        return list(ans)
