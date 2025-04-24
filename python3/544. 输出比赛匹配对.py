class Solution:

    def findContestMatch(self, n: int) -> str:

        q = list(map(str, range(1, n+1)))
        while True:
            qq = list()
            while len(q) > 1:
                f = q.pop(0)
                e = q.pop(-1)
                qq.append("({},{})".format(f, e))
            if len(q):
                qq.append(q)
            qq = sorted(qq, key=lambda x: int(x.split(",")[0].split("(")[-1]))
            if len(qq) == 1:
                break
            q = qq

        return "".join(qq)
