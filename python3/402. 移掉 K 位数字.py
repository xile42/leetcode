class Solution:

    def removeKdigits(self, num: str, k: int) -> str:

        n = len(num)
        if n == k:
            return "0"

        st = list()
        chance = k
        for c in num:
            while st and c < st[-1] and chance:
                st.pop(-1)
                chance -= 1
            st.append(c)

        ans = "".join(st)
        while ans and ans[0] == "0":
            ans = ans[1:]

        while chance and ans:
            ans = ans[:-1]
            chance -= 1

        return "0" if not ans else ans
