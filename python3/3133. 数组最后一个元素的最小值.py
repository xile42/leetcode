class Solution:

    def minEnd(self, n: int, x: int) -> int:

        if n == 1:
            return x

        template = bin(n - 1)[2:]
        bx = bin(x)[2:]
        ans = []

        jdx = -1
        i = 0
        while i < x.bit_length() or abs(jdx) <= len(template):
            if x & (1 << i):
                ans.append(bx[-(i + 1)])
            else:
                if abs(jdx) <= len(template):
                    ans.append(template[jdx])
                else:
                    ans.append("0")
                jdx -= 1
            i += 1

        return int("".join(ans[::-1]), 2)
