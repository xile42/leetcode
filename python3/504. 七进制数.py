class Solution:

    def convertToBase7(self, num: int) -> str:

        if num == 0:
            return "0"

        cur = abs(num)
        ans = list()
        while cur:
            ans.append(str(cur % 7))
            cur //= 7

        ans = "".join(ans[::-1])
        ans = "-" + ans if num < 0 else ans

        return ans
        
