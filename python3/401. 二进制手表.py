class Solution:

    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        hs = [8, 4, 2, 1]
        ms = [32, 16, 8, 4, 2, 1]
        ans = set()
        for i in range(turnedOn + 1):
            j = turnedOn - i
            if i > len(hs) or j > len(ms):
                continue
            for hvs in combinations(hs, i):
                for mvs in combinations(ms, j):
                    h = 0 if not hvs else sum(hvs)
                    m = 0 if not mvs else sum(mvs)
                    if h < 12 and m < 60:
                        ans.add(tuple([h, m]))

        ans = ["{}:{}".format(str(h), "0" + str(m) if m < 10 else str(m)) for h, m in ans]

        return ans
