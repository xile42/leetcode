class Solution:

    def interpret(self, command: str) -> str:

        st = list()
        result = list()
        for char in command:
            if char == "G":
                result.append("G")
                continue
            elif char == ")":
                if st[-1] == "(":
                    result.append("o")
                    continue
                else:
                    part = list()
                    while st[-1] != "(":
                        part.append(st.pop(-1))
                    st.pop(-1)
                    result.append("".join(part[::-1]))
                    continue
            else:
                st.append(char)

        return "".join(result)
