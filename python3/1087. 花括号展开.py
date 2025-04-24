class Solution:

    def expand(self, s: str) -> List[str]:

        st = list()
        parts = list()
        flag = False
        for char in s:
            if char == ",":
                continue
            elif char == "}":
                part = list()
                while st and st[-1] != "{":
                    part.append(st.pop(-1))
                st.pop(-1)
                parts.append(part)
                flag = False
            elif char == "{":
                flag = True
                st.append(char)
            else:
                if not flag:
                    parts.append([char])
                else:
                    st.append(char)

        results = list()

        def f(parts, cur):

            if len(parts) == 0:
                results.append(cur)
                return 

            for char in parts[0]:
                f(parts[1:], cur + char)

        f(parts, "")
        results = sorted(results)

        return results
        
