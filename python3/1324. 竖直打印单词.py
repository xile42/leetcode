class Solution:

    def printVertically(self, s: str) -> List[str]:

        s = s.split()

        n = max(len(i) for i in s)

        ans = list()
        for i in range(n):
            this_ans = list()
            for w in s:
                if i < len(w):
                    this_ans.append(w[i])
                else:
                    this_ans.append(" ")
            ans.append("".join(this_ans).rstrip())

        return ans
