class Solution:

    def maxDiff(self, num: int) -> int:

        sn = str(num)
        s = set(sn)

        if s == {"9"}:
            mx = num
        else:
            for i, c in enumerate(sn):
                if c != "9":
                    tar = c
                    break
            mx = int(sn.replace(tar, "9"))

        mn = num
        for c in s:
            for tar in ["1", "0"]:
                mn_s = sn.replace(c, tar)
                if mn_s[0] == "0" or int(mn_s) == 0:
                    continue
                mn = min(mn, int(mn_s))

        return mx - mn
