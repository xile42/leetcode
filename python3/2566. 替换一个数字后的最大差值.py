class Solution:

    def minMaxDifference(self, num: int) -> int:

        sn = str(num)

        tar = None
        for c in sn:
            if c != "9":
                tar = c
                break
        mx = int(sn) if tar is None else int(sn.replace(tar, "9"))

        tar = None
        for c in sn:
            if c != "0":
                tar = c
                break
        mn = int(sn) if tar is None else int(sn.replace(tar, "0"))

        return mx - mn
