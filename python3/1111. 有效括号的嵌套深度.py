class Solution:

    def maxDepthAfterSplit(self, seq: str) -> List[int]:

        n = len(seq)
        ans = list()
        cur = 0
        for c in seq:
            if c == "(":
                cur += 1
                ans.append(cur & 1)
            else:
                ans.append(cur & 1)
                cur -= 1

        return ans
