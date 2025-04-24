class Solution:

    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        l = [widths[ord(i)-ord("a")] for i in s]
        cnt = 1
        cur = 0
        idx = 0
        while idx < len(l):
            if cur + l[idx] <= 100:
                cur += l[idx]
                idx += 1
            else:
                cnt += 1
                cur = l[idx]
                idx += 1

        return [cnt, cur]
