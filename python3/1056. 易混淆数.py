class Solution:

    def confusingNumber(self, n: int) -> bool:

        if len(set(str(n)) - {"0", "1", "9", "8", "6"}) != 0:
            return False

        s, rs = str(n), str(n)[::-1]
        d = {"0": "0", "1": "1", "9": "6", "8": "8", "6": "9"}

        if not all(c == d[rc] for c, rc in zip(s, rs)):
            return True

        return False
