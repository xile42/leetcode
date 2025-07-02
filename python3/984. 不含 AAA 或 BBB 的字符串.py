class Solution:

    def strWithout3a3b(self, a: int, b: int) -> str:

        ans = str()

        for _ in range(a + b):
            if (len(ans) >= 2 and ans[-1] == 'b' and ans[-2] == 'b') or (a > b and not (len(ans) >= 2 and ans[-1] == 'a' and ans[-2] == 'a')):
                ans += 'a'
                a -= 1
            else:
                ans += 'b'
                b -= 1

        return ans
