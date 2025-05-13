class Solution:

    def minimizeXor(self, num1: int, num2: int) -> int:

        n1, n2 = num1.bit_count(), num2.bit_count()
        if n1 == n2:
            return num1
        if n1 > n2:
            pos1 = list()
            for i in range(32):
                if num1 & (1 << i):
                    pos1.append(i)
                if len(pos1) >= n1 - n2:
                    break
            for i in pos1[:n1 - n2]:
                num1 ^= 1 << i
            return num1
        else:
            for _ in range(n2 - n1):
                for i in range(32):
                    if num1 & (1 << i) == 0:
                        num1 |= 1 << i
                        break
            return num1