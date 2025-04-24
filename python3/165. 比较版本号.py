class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:

        v1s = list(map(int, version1.split(".")))
        v2s = list(map(int, version2.split(".")))
        l1, l2 = len(v1s), len(v2s)
        l = max(l1, l2)

        for i in range(l):
            v1 = 0 if i >= l1 else v1s[i]
            v2 = 0 if i >= l2 else v2s[i]
            if v1 == v2:
                continue
            elif v1 < v2:
                return -1
            else:
                return 1

        return 0
