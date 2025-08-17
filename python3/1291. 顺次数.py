class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:

        ans = list()

        for d in range(9, 0, -1):
            s = str(d)
            while int(s) <= high:
                if int(s) >= low:
                    ans.append(int(s))
                next_c = str(int(s[0]) - 1)
                if next_c == "0":
                    break
                s = next_c + s

        return sorted(ans)
