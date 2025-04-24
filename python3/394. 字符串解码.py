class Solution:

    def decodeString(self, s: str) -> str:

        st = list()
        for char in s:
            if char == "]":
                sub = ""
                while st and st[-1] != "[":
                    sub += st.pop(-1)
                st.pop(-1)
                num = ""
                while st and st[-1].isdigit():
                    num += st.pop(-1)
                sub = sub[::-1] * int(num[::-1])
                st += sub
            else:
                st.append(char)

        return "".join(st)
