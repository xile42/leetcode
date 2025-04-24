import re


class Solution:

    def calculate(self, s: str) -> int:

        st = list()
        n = str()
        pre = "+"
        s = s.strip()
        for i, c in enumerate(s):
            if c == " ":
                continue
            if c.isdigit():
                n += c
            if not c.isdigit() or i == len(s) - 1:
                if pre == "+":
                    st.append(int(n))
                elif pre == "-":
                    st.append(-int(n))
                elif pre == "*":
                    st[-1] *= int(n)
                elif pre == "/":
                    st[-1] = st[-1] // int(n) if st[-1] >= 0 else -(abs(st[-1]) // int(n))
                else:
                    print(pre)
                pre = c
                n = str()

        return sum(st)                
        

##        nums = list(map(int, re.findall(r"[\d]+", s)))
##        ops = [c for c in s if c in ["+", "-", "*", "/"]]
##        st = list()
##        st.append(nums[0])
##        for idx in range(len(ops)):
##            op, n = ops[idx], nums[idx + 1]
##            if op in ["+", "-"]:
##                st += [op, n]
##            elif op == "*":
##                st[-1] = st[-1] * n
##            else:
##                st[-1] = st[-1] // n
##
##        n1 = st[0]
##        st = st[1:]
##        while len(st):
##            op, n2 = st[:2]
##            st = st[2:]
##            if op == "+":
##                n1 += n1 + n2
##            else:
##                n1 += n1 - n2
##
##        return n1
