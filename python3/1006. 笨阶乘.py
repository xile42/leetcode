from operator import *


class Solution:

    def clumsy(self, n: int) -> int:

        ns = list(range(1, n + 1))[::-1]
        ops = [mul, floordiv, add, sub]
        cur = 0
        st = [ns[0]]
        for j in ns[1:]:
            op = ops[cur]
            if cur <= 1:
                i = st.pop(-1)
                st.append(op(i, j))
            else:
                st.append(op)
                st.append(j)
            cur += 1
            cur %= len(ops)

        ans = st[0]
        cur = 1
        while cur < len(st):
            op = st[cur]
            j = st[cur + 1]
            ans = op(ans, j)
            cur += 2

        return ans
