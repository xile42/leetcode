class Solution:

    def evalRPN(self, tokens: List[str]) -> int:

        st = list()
        for c in tokens:
            if c == "+":
                v = st[-2] + st[-1]
                st = st[:-2] + [v]
            elif c == "-":
                v = st[-2] - st[-1]
                st = st[:-2] + [v]
            elif c == "*":
                v = st[-2] * st[-1]
                st = st[:-2] + [v]
            elif c == "/":
                v = int(float(st[-2]) / float(st[-1]))
                st = st[:-2] + [v]
            else:
                st.append(int(c))

        return st[0]
