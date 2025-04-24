class Solution:

    def getSmallestString(self, s: str) -> str:

        result = str()
        flag = False
        for idx in range(len(s) - 1):
            a, b = int(s[idx]), int(s[idx+1])
            if a & 1 == b & 1 and a > b:
                flag = True
                result += s[idx+1]
                result += s[idx]
                result += s[idx+2:]
                break
            else:
                result += s[idx]
        if not flag:
            result += s[-1]

        return result
