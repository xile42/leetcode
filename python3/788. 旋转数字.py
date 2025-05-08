class Solution:

    def rotatedDigits(self, n: int) -> int:

        ans = 0
        d = {
            "2": "5",
            "5": "2",
            "0": "0",
            "8": "8",
            "6": "9",
            "9": "6",
            "1": "1",
        }

        def check(s):

            ans = str()
            for c in s:
                if c not in d:
                    return False
                ans += d[c]

            return int(s) != int(ans)

        for i in range(1, n + 1):
            if check(str(i)):
                ans += 1

        return ans
