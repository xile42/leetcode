class Solution:

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        ns = list()
        l, la, lb = len(s), len(a), len(b)
        for i in range(l - la + 1):
            if s[i:i + la] == a:
                ns.append([i, 0])
        for i in range(l - lb + 1):
            if s[i:i + lb] == b:
                ns.append([i, 1])
                ns.append([i, -1])

        ns.sort()

        pre = [inf] * l
        suf = [inf] * l
        cur = None
        for idx in range(len(ns)):
            i, flag = ns[idx]
            if flag == -1:
                cur = i
            elif flag == 0:
                if cur is not None:
                    pre[i] = cur
        cur = None
        for idx in range(len(ns) - 1, -1, -1):
            i, flag = ns[idx]
            if flag == 1:
                cur = i
            elif flag == 0:
                if cur is not None:
                    suf[i] = cur

        ans = list()
        for i, flag in ns:
            if flag == 0:
                if abs(pre[i] - i) <= k or abs(suf[i] - i) <= k:
                    ans.append(i)

        return ans
